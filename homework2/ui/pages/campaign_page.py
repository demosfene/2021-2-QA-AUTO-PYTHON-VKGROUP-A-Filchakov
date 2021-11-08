import click as click

from ui.locators.basic_locators import CampaignPageLocators
from ui.pages.base_page import BasePage


class CampaignPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = CampaignPageLocators

    def create_new_company(self, file_path):
        self.click(self.locators.CREATE_COMPANY_BUTTON_LOCATOR, 10)
        self.click(self.locators.TRAFFIC_BUTTON_LOCATOR, 10)
        url_field = self.find(self.locators.URL_COMPANY_FIELD_LOCATOR, 10)
        url_field.send_keys(self.url)
        self.click(self.locators.BANNER_LOCATOR, 10)
        upload_picture = self.find(self.locators.INPUT_PICT_LOCATOR, 10)
        upload_picture.send_keys(file_path)
        self.click(self.locators.BUTTON_SUBMIT_LOCATOR, 10)

    def delete_campaign(self, campaign_id):
        self.click(self.locators.SETTINGS_BY_ID_LOCATOR(campaign_id), 10)

