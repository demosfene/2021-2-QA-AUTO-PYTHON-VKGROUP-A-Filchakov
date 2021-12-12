import pytest

from mysql_orm.client import MysqlORMClient


def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()
    mysql_orm_client.connect(db_created=True)

    config.mysql_orm_client = mysql_orm_client


def pytest_addoption(parser):
    parser.addoption('--file', default='C:\\Users\\Professional\\PycharmProjects\\repo\homework6\\test_sql_orm\\access.log')


@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MysqlORMClient:
    client = request.config.mysql_orm_client

    yield client
    client.connection.close()

@pytest.fixture(scope='session')
def file_path(request):
    file = request.config.getoption('--file')
    yield file
