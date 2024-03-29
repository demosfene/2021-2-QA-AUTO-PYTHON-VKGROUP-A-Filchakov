import logging
import uuid
from urllib.parse import urljoin

import requests

logger = logging.getLogger('test')
MAX_RESPONSE_LENGTH = 666


class InvalidLoginException(Exception):
    pass


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url, user, password, data, locations):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.data_body = data
        self.locations = locations

        self.session = requests.Session()
        self.mc = None
        self.sdc = None
        self.csrftoken = None

    @property
    def post_headers(self):
        return {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

    def redirect_request(self, redirect, method, request_url, headers, data):
        response = None
        while redirect:
            response = self.session.request(method, request_url, headers=headers, data=data,
                                            allow_redirects=not redirect)
            if 'Set-Cookie' in response.headers:
                response_cookies = response.headers['Set-Cookie'].split(';')
                for cookie in response_cookies:
                    if 'mc' in cookie:
                        self.mc = cookie.split('=')[-1]
                    elif 'sdc' in cookie:
                        self.sdc = cookie.split('=')[-1]
            redirect = response.is_redirect
            if redirect:
                request_url = response.next.url
                method = response.next.method
                headers = response.next.headers
        return response

    def _request(self, method, location='', url=None, headers=None, data=None,
                 redirect=False, json_data=None):
        request_url = urljoin(self.base_url if url is None else url, location)
        if redirect:
            response = self.redirect_request(redirect, method, request_url, headers, data)
        else:
            response = self.session.request(method, request_url, headers=headers, data=data, json=json_data)
        return response

    def login(self):
        headers_post = {
            'Referer': 'https://target.my.com/',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        headers_get = {
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1',
            'failure': 'https://account.my.com/login/'
        }

        self._request(method='POST', url='https://auth-ac.my.com/auth', headers=headers_post, data=data,
                      redirect=True)
        response_csrftoken = self._request('GET', self.locations['csrf'], headers=headers_get)
        assert response_csrftoken.status_code == 200
        response_cookies = response_csrftoken.headers['Set-Cookie'].split(';')
        self.csrftoken = [c for c in response_cookies if 'csrftoken' in c][0].split('=')[-1]

        headers = headers_post
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'

        auth_user = self._request(method='GET', location='/api/v3/user.json', headers=headers)

        return auth_user.status_code == 200

    def create_campaign(self):
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken

        data_campaign = eval(self.data_body['campaign'])
        campaign_name = str(uuid.uuid4())
        data_campaign['name'] = campaign_name

        response = self._request('POST', self.locations['create_campaigns'], headers=headers, json_data=data_campaign)
        return {'response': response, 'campaign_name': campaign_name}

    def create_segment(self):
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'

        data_segment = eval(self.data_body['segment'])
        segment_name = str(uuid.uuid4())
        data_segment['name'] = segment_name

        response = self._request(method='POST', location=self.locations['create_segments'], headers=headers,
                                 json_data=data_segment)
        return {'response': response, 'segment_name': segment_name}

    def get_segment(self, segment_id):
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'
        response = self._request(method='GET', location=self.locations['get_segment'].format(segment_id),
                                 headers=headers)

        return response

    def get_campaign(self, campaign_id):
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'
        response = self._request(method='GET', location=self.locations['get_campaign'].format(campaign_id["id"]),
                                 headers=headers)

        return response

    def delete_segment(self, segment_id):
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'

        response = self._request('DELETE', location=self.locations['delete_segment'].format(segment_id),
                                 headers=headers)
        return response

    def delete_campaign(self, campaign_id):
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'

        response = self._request('DELETE', location=self.locations['delete_campaign'].format(campaign_id["id"]),
                                 headers=headers)
        return response
