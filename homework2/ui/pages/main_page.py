from ui.locators.basic_locators import MainPageLocators
from ui.pages.audience_page import AudiencePage
from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage


class MainPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = MainPageLocators()

    def go_to_campaign_page(self):
        self.click(self.locators.CAMPAIGN_PAGE_LOCATOR, 10)
        return CampaignPage(self.driver)

    def go_to_audience_page(self):
        self.click(self.locators.AUDIENCE_PAGE_LOCATOR, 10)
        return AudiencePage(self.driver)

