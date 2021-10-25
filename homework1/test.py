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

    def test_login(self, login_init):
        assert "Кампании" in self.driver.title
        assert 'https://target.my.com/dashboard' in self.driver.current_url

    def test_logout(self, login_init):
        self.logout()

        assert "Рекламная платформа myTarget — Сервис таргетированной рекламы" in self.driver.title
        assert 'https://target.my.com/' in self.driver.current_url

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
        "locator,url",
        [
            (basic_locators.BILLING_LOCATOR, 'https://target.my.com/billing'),
            (basic_locators.STATISTICS_LOCATOR, 'https://target.my.com/statistics')
        ]
    )
    def test_go_to_page(self, login_init, locator, url):
        self.click(locator)

        assert url in self.driver.current_url
