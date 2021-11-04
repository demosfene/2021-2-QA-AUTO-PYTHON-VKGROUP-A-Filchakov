import os

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver

from ui.fixtures import *
from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

CLICK_RETRY = 3


class BaseCase:

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.config = config
        self.logger = logger
        self.base_page: BasePage = request.getfixturevalue('base_page')

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')

            for cookie in cookies:
                cookie['sameSite'] = 'Strict'
                self.driver.add_cookie(cookie)

            self.driver.refresh()
            self.main_page: MainPage = request.getfixturevalue('main_page')
        else:
            self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.logger.debug('Initial setup completed')
