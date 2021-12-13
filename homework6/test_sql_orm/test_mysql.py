from test_sql_orm.data_file import get_data, top_by_conn_5xx, count_by_length_4xx, count_by_url, count_by_types, count
from models.model import CountRequest, CountRequestByType, CountRequestByUrl, CountRequestByLength4xx, \
    CountRequestByUsers5xx
from test_sql_orm.base import MysqlBase


class TestHomework5TotalConnections(MysqlBase):
    top = 0

    def prepare(self):
        self.mysql.create_count_requests('count_requests')
        data = count(self.file)
        self.top = len(data)
        self.mysql_builder.create_count_request(data['total_connections'])

    def test_total_connections(self):
        assert self.mysql.session.query(CountRequest).count() == self.top


class TestHomework5CountByTypes(MysqlBase):
    top = 0

    def prepare(self):
        self.mysql.create_count_requests('count_request_of_type')
        data = count_by_types(self.file)
        self.top = len(data['count_by_types'])
        for con in data['count_by_types']:
            self.mysql_builder.create_count_request_of_type(con, data['count_by_types'][con])

    def test_count_by_types(self):
        assert self.mysql.session.query(CountRequestByType).count() == self.top


class TestHomework5TopByUrls(MysqlBase):
    top = 10

    def prepare(self):
        self.mysql.create_count_requests('count_request_of_url')
        data = count_by_url(self.top, self.file)
        if len(data['top_by_urls']) < self.top:
            self.top = len(data['top_by_urls'])
        for con in data['top_by_urls']:
            self.mysql_builder.create_count_request_of_url(urls=con, requests_count=data['top_by_urls'][con])

    def test_top_by_urls(self):
        assert self.mysql.session.query(CountRequestByUrl).count() == self.top


class TestHomework5TopByLength4xx(MysqlBase):
    top = 10

    def prepare(self):
        self.mysql.create_count_requests('count_request_of_length_4xx')
        data = count_by_length_4xx(self.top, self.file)
        if len(data['top_by_length_4xx']) < self.top:
            self.top = len(data['top_by_length_4xx'])
        for con in data['top_by_length_4xx']:
            self.mysql_builder.create_count_request_of_length_4xx(urls=con,
                                                                  status_code=int(data['top_by_length_4xx'][con][
                                                                                      'status_code']),
                                                                  length=int(
                                                                      data['top_by_length_4xx'][con]['length']),
                                                                  ip=data['top_by_length_4xx'][con]['ip'])

    def test_top_by_length_4xx(self):
        assert self.mysql.session.query(CountRequestByLength4xx).count() == self.top


class TestHomework5TopByTopCount5xx(MysqlBase):
    top = 10

    def prepare(self):
        self.mysql.create_count_requests('count_request_of_users_5xx')
        data = top_by_conn_5xx(self.top, self.file)
        if len(data['top_by_conn_count_5xx']) < self.top:
            self.top = len(data['top_by_conn_count_5xx'])
        for con in data['top_by_conn_count_5xx']:
            self.mysql_builder.create_count_request_of_users_5xx(ip=con,
                                                                 requests_count=int(
                                                                     data['top_by_conn_count_5xx'][con]['count']))

    def test_top_by_conn_count_5xx(self):
        assert self.mysql.session.query(CountRequestByUsers5xx).count() == self.top
