import random
import string

from base import BaseCase
from ui.fixtures import *


class TestLoginFailure(BaseCase):

    @pytest.mark.UI
    def test_create_traffic_campaign(self, file_path):
        campaign_page = self.main_page.go_to_campaign_page()
        campaign_page.create_new_campaign(file_path)
        assert campaign_page.find(campaign_page.locators.NOTIFY_SUCCESS_CREATE_CAMPAIGN_LOCATOR, 10)

    @pytest.mark.UI
    def test_create_segment(self):
        audience_page = self.main_page.go_to_audience_page()
        id_segment = audience_page.create_new_segment()

        assert id_segment
        audience_page.remove_segment(id_segment)

    @pytest.mark.UI
    def test_remove_segment(self):
        audience_page = self.main_page.go_to_audience_page()
        id_segment = audience_page.create_new_segment()

        assert audience_page.remove_segment(id_segment)


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.UI
    def test_login_incorrect_email(self):
        self.login_page.login(random.choice(string.ascii_letters), str(random.randint(1, 1000)),
                              self.login_page.locators)
        assert self.login_page.find(self.login_page.locators.NOTIFY_ERROR_LOCATOR, 5)

    @pytest.mark.UI
    def test_login_incorrect_password(self):
        self.login_page.login(random.choice(string.ascii_letters), ' ',
                              self.login_page.locators)
        assert self.login_page.find(self.login_page.locators.NOTIFY_ERROR_LOCATOR, 5)
