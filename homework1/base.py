import configparser

import pytest
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException

WAIT_TIMEOUT = 20
RETRY_COUNT = 5

config = configparser.ConfigParser()
config.read("settings.ini")


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def enter_text_in_field(self, locator, text):
        field = self.find(locator)
        field.send_keys(text)

    def enter_text_in_field_with_clear(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def click(self, locator):
        element = WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.presence_of_element_located(locator))
        element.click()

    def click_with_retry_and_wait(self, locator, retry_count, exceptions):
        sleep(3)
        for i in range(retry_count):
            try:
                element = WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.presence_of_element_located(locator))
                element.click()
            except exceptions as e:
                if i == retry_count - 1:
                    raise
                else:
                    print(f'Got exception {e}, try: {i}')
                    sleep(3)
                    pass
            else:
                return

    def click_with_wait_to_be_clickable(self, locator):
        element = WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable(locator))
        element.click()

    def login(self, email, password):
        self.click(basic_locators.LOGIN_LOCATOR)
        self.enter_text_in_field(basic_locators.LOGIN_EMAIL_LOCATOR, email)
        self.enter_text_in_field(basic_locators.LOGIN_PASSWORD_LOCATOR, password)
        self.enter_text_in_field(basic_locators.LOGIN_PASSWORD_LOCATOR, Keys.ENTER)

    def logout(self):
        self.click(basic_locators.ACCOUNT_ACTIONS_LOCATOR)
        self.click_with_retry_and_wait(basic_locators.ACCOUNT_LOGOUT_LOCATOR, RETRY_COUNT,
                                       (ElementNotInteractableException, StaleElementReferenceException,
                                        ElementClickInterceptedException))
