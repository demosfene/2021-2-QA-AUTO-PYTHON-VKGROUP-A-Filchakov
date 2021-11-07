import os
import shutil
import sys

import configparser

from api.client import ApiClient
from ui.fixtures import *

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "settings.ini"))


@pytest.fixture(scope='session')
def credentials():
    user = config['User']['email']
    password = config['User']['password']

    return user, password


@pytest.fixture(scope='session')
def api_client(credentials):
    return ApiClient(config['Url']['main_url'], *credentials)
