import pytest
from _pytest.fixtures import FixtureRequest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# from ui.fixtures import credentials
from ui.pages.main_page import MainPage
from ui.locators.basic_locators import LoginPageLocators
from ui.pages.base_page import BasePage


#
class LoginPage(BasePage):
    url = 'https://target.my.com/'
    locators = LoginPageLocators

    def login(self, user, password, login_locator=locators):
        self.click(login_locator.LOGIN_LOCATOR, 10)
        email_field = self.find(login_locator.LOGIN_EMAIL_LOCATOR)
        email_field.send_keys(user)
        password_field = self.find(login_locator.LOGIN_PASSWORD_LOCATOR)
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        try:
            self.driver.execute_script('return arguments[0].firstChild.textContent;',
                                       self.find(login_locator.NOTIFY_ERROR_LOCATOR, 1))
            return self
        except TimeoutException:
            return MainPage(self.driver)

    def login_init(self, credentials):
        self.login(*credentials, self.locators)
