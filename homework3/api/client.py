import json
import logging
import uuid
from time import sleep
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

    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password

        self.session = requests.Session()
        self.mc = None
        self.sdc = None
        self.csrftoken = None

    @property
    def post_headers(self):
        return {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

    def get_new_data(self, location):
        name = uuid.uuid4()
        data = None
        if 'campaigns' in location:
            data = {"name": str(name), "read_only": False, "conversion_funnel_id": None,
                    "objective": "traffic", "enable_offline_goals": False,
                    "targetings": {"split_audience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "sex": ["male", "female"],
                                   "age": {
                                       "age_list": [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                                                    28, 29, 30, 31, 32,
                                                    33, 34,
                                                    35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                                                    52, 53, 54, 55, 56,
                                                    57,
                                                    58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                                                    75],
                                       "expand": True},
                                   "geo": {"regions": [188]}, "interests_soc_dem": [], "segments": [], "interests": [],
                                   "fulltime": {"flags": ["use_holidays_moving", "cross_timezone"],
                                                "mon": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18,
                                                        19, 20,
                                                        21, 22, 23],
                                                "tue": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18,
                                                        19, 20,
                                                        21, 22, 23],
                                                "wed": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18,
                                                        19, 20,
                                                        21, 22, 23],
                                                "thu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18,
                                                        19, 20,
                                                        21, 22, 23],
                                                "fri": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18,
                                                        19, 20,
                                                        21, 22, 23],
                                                "sat": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18,
                                                        19, 20,
                                                        21, 22, 23],
                                                "sun": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18,
                                                        19, 20,
                                                        21, 22, 23]}, "pads": [102643],
                                   "mobile_types": ["tablets", "smartphones"],
                                   "mobile_vendors": [], "mobile_operators": []}, "age_restrictions": None,
                    "date_start": None,
                    "date_end": None, "autobidding_mode": "second_price_mean", "budget_limit_day": None,
                    "budget_limit": None,
                    "mixing": "fastest", "utm": None, "enable_utm": True, "price": "4.04", "max_price": "0",
                    "package_id": 961,
                    "banners": [
                        {"urls": {"primary": {"id": 6584979}}, "textblocks": {},
                         "content": {"image_240x400": {"id": 9690553}},
                         "name": ""}]}
        elif 'segments' in location:
            data = {"name":str(name), "pass_condition": 1, "relations": [
                {"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}},
                {"object_type": "remarketing_payer", "params": {"type": "positive", "left": 365, "right": 0}}],
                    "logicType": "or"}
        return data

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
        location = '/csrf'
        response_csrftoken = self._request('GET', location, headers=headers_get)
        response_cookies = response_csrftoken.headers['Set-Cookie'].split(';')
        self.csrftoken = [c for c in response_cookies if 'csrftoken' in c][0].split('=')[-1]

        location = '/dashboard'

        headers = headers_post
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'

        response = self._request(method='POST', location=location, headers=headers)

        find_login_on_page = response.text.find(f'data-ga-auth-username="{self.user}"')

        return self.sdc is not None and self.mc is not None and self.csrftoken is not None and find_login_on_page != -1

    def create_campaign(self):
        location = '/api/v2/campaigns.json'
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken

        data = self.get_new_data(location)

        response_1 = self._request('POST', location, headers=headers, json_data=data)
        return json.loads(response_1.text)
        # ['banners'][0]['id']

    def create_segment(self):
        location = '/api/v2/remarketing/segments.json'

        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'

        data = self.get_new_data(location)

        response = self._request(method='POST', location=location, headers=headers, json_data=data)
        return json.loads(response.text)["id"]

    def get_segment(self, segment_id):
        location = f'/api/v2/remarketing/segments/{segment_id}.json'
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'
        response = self._request(method='GET', location=location, headers=headers)

        return response

    def get_campaign(self, campaign_id):
        location = f'/api/v2/campaigns/{campaign_id["id"]}.json?fields=name,id,status'
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'
        response = self._request(method='GET', location=location, headers=headers)

        return response.json()

    def delete_segment(self, segment_id):
        location = f'/api/v2/remarketing/segments/{segment_id}.json'

        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'

        response = self._request('DELETE', location=location, headers=headers)
        return response

    def delete_campaign(self, campaign_id):
        location = f'/api/v2/campaigns/{campaign_id["id"]}.json'

        headers = self.post_headers
        headers['Cookie'] = f'mc={self.mc}; sdc={self.sdc}; csrftoken={self.csrftoken}'
        headers['X-CSRFToken'] = self.csrftoken
        headers['Content-Type'] = 'application/json'

        response = self._request('DELETE', location=location, headers=headers)
        return response
