import random
from base import BaseCase, config
from ui.locators import basic_locators
from time import sleep
import pytest


class TestOne(BaseCase):

    @pytest.fixture(scope='function')
    def login_init(self):
        email = config['User']['email']
        password = config['User']['password']
        assert email and password
        self.login(email, password)
        sleep(3)

    @pytest.mark.UI
    def test_login(self, login_init):

        assert self.find(basic_locators.LOGIN_DONE_PAGE_LOCATOR)

    @pytest.mark.UI
    def test_logout(self, login_init):
        self.logout()

        assert self.find(basic_locators.MAIN_PAGE_LOCATOR)

    @pytest.mark.UI
    def test_edit_user_info(self, login_init):
        self.click(basic_locators.PROFILE_LOCATOR)
        sleep(3)
        self.click(basic_locators.FIO_LOCATOR)

        new_name = str(random.randint(1, 1000))
        self.enter_text_in_field_with_clear(basic_locators.FIO_LOCATOR, new_name)
        self.click(basic_locators.BUTTON_SAVE_LOCATOR)
        self.driver.refresh()
        sleep(5)

        assert str(self.find(basic_locators.FIO_LOCATOR).get_attribute("value")) == new_name

    @pytest.mark.parametrize(
        "locator,class_locator",
        [
            (basic_locators.BILLING_MENU_LOCATOR, basic_locators.BILLING_CLASS_LOCATOR),
            (basic_locators.STATISTICS_MENU_LOCATOR, basic_locators.STATISTICS_CLASS_LOCATOR)
        ]
    )
    @pytest.mark.UI
    def test_go_to_page(self, login_init, locator, class_locator):
        self.click(locator)

        assert self.find(class_locator)
