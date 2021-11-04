import os

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

CLICK_RETRY = 3


class BaseCase:

    driver = None

    # @pytest.fixture(scope='function', autouse=True)
    # def ui_report(self, driver, request, temp_dir):
    #     failed_tests_count = request.session.testsfailed
    #     yield
    #     if request.session.testsfailed > failed_tests_count:
    #         screenshot = os.path.join(temp_dir, 'failure.png')
    #         driver.get_screenshot_as_file(screenshot)
    #         allure.attach.file(screenshot, 'failure.png', attachment_type=allure.attachment_type.PNG)
    #
    #         browser_log = os.path.join(temp_dir, 'browser.log')
    #         with open(browser_log, 'w') as f:
    #             for i in driver.get_log('browser'):
    #                 f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
    #
    #         with open(browser_log, 'r') as f:
    #             allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')

        self.logger.debug('Initial setup completed')
        
