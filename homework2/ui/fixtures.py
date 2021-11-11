import logging

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from files import constant
from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage


@pytest.fixture(scope='session')
def credentials():
    user = constant.user
    password = constant.password

    return user, password


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture(scope='function')
def login_page_init(driver, credentials):
    LoginPage(driver=driver).login_init(credentials)
    return


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)


def get_driver(config):
    browser_name = config['browser']

    if browser_name == 'chrome':
        options = Options()
        manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
        browser = webdriver.Chrome(executable_path=manager.install(), options=options)

    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = config['url']
    with allure.step('Init browser'):
        browser = get_driver(config)
        browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config)
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookies = driver.get_cookies()
    driver.quit()
    return cookies
