import os

import configparser

from api.client import ApiClient
from ui.fixtures import *

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "settings.ini"))


@pytest.fixture(scope='session')
def credentials():
    user = config['User']['email']
    password = config['User']['password']
    data = config['Data']
    locations = config['Locations']
    return user, password, data, locations


@pytest.fixture(scope='session')
def api_client(credentials):
    return ApiClient(config['Url']['main_url'], *credentials)
