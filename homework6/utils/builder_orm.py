from models.model import CountRequest, CountRequestByType, CountRequestByUrl, CountRequestByLength4xx, \
    CountRequestByUsers5xx


class MysqlORMBuilder:

    def __init__(self, client):
        self.client = client

    def create_count_request(self, requests_count):
        requests_count = CountRequest(
            requests_count=requests_count
        )

        self.client.session.add(requests_count)
        self.client.session.commit()
        return requests_count

    def create_count_request_of_type(self, requests_method, requests_count):
        requests_count_of_type = CountRequestByType(
            type=requests_method,
            requests_count=requests_count
        )

        self.client.session.add(requests_count_of_type)
        self.client.session.commit()
        return requests_count_of_type

    def create_count_request_of_url(self, urls, requests_count):
        requests_count_of_url = CountRequestByUrl(
            urls=urls,
            requests_count=requests_count
        )

        self.client.session.add(requests_count_of_url)
        self.client.session.commit()
        return requests_count_of_url

    def create_count_request_of_length_4xx(self, urls, status_code, length, ip):
        requests_count_of_length_4xx = CountRequestByLength4xx(
            urls=urls,
            status_code=status_code,
            length=length,
            ip=ip
        )

        self.client.session.add(requests_count_of_length_4xx)
        self.client.session.commit()
        return requests_count_of_length_4xx

    def create_count_request_of_users_5xx(self, ip, requests_count):
        requests_count_of_users_5xx = CountRequestByUsers5xx(
            ip=ip,
            requests_count=requests_count
        )

        self.client.session.add(requests_count_of_users_5xx)
        self.client.session.commit()
        return requests_count_of_users_5xx
