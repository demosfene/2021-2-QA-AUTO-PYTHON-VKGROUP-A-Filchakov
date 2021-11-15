from test_sql_orm.data_file import get_data
from models.model import CountRequest, CountRequestByType, CountRequestByUrl, CountRequestByLength4xx, \
    CountRequestByUsers5xx
from test_sql_orm.base import MysqlBase


class TestHomework5TotalConnections(MysqlBase):

    def prepare(self):
        data = get_data()
        self.mysql_builder.create_count_request(data['total_connections'])

    def test_total_connections(self):
        print(self.mysql.session.query(CountRequest).all())
        assert self.mysql.session.query(CountRequest).count() == 1


class TestHomework5CountByTypes(MysqlBase):

    def prepare(self):
        data = get_data()
        for con in data['count_by_types']:
            self.mysql_builder.create_count_request_of_type(con, data['count_by_types'][con])

    def test_count_by_types(self):
        print(self.mysql.session.query(CountRequestByType).all())
        assert self.mysql.session.query(CountRequestByType).count() == 4


class TestHomework5TopByUrls(MysqlBase):

    def prepare(self):
        data = get_data()
        for con in data['top_by_urls']:
            self.mysql_builder.create_count_request_of_url(urls=con, requests_count=data['top_by_urls'][con])

    def test_top_by_urls(self):
        print(self.mysql.session.query(CountRequestByUrl).all())
        assert self.mysql.session.query(CountRequestByUrl).count() == 10


class TestHomework5TopByLength4xx(MysqlBase):

    def prepare(self):
        data = get_data()
        for con in data['top_by_length_4xx']:
            self.mysql_builder.create_count_request_of_length_4xx(urls=con,
                                                                  status_code=int(data['top_by_length_4xx'][con][
                                                                                      'status_code']),
                                                                  length=int(
                                                                      data['top_by_length_4xx'][con]['length']),
                                                                  ip=data['top_by_length_4xx'][con]['ip'])

    def test_top_by_length_4xx(self):
        print(self.mysql.session.query(CountRequestByLength4xx).all())
        assert self.mysql.session.query(CountRequestByLength4xx).count() == 5


class TestHomework5TopByTopCount5xx(MysqlBase):

    def prepare(self):
        data = get_data()
        for con in data['top_by_conn_count_5xx']:
            self.mysql_builder.create_count_request_of_users_5xx(ip=con,
                                                                 requests_count=int(
                                                                     data['top_by_conn_count_5xx'][con]['count']))

    def test_top_by_conn_count_5xx(self):
        print(self.mysql.session.query(CountRequestByUsers5xx).all())
        assert self.mysql.session.query(CountRequestByUsers5xx).count() == 5
