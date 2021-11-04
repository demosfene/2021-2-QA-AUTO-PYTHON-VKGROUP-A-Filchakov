from ui.locators.basic_locators import CompanyPageLocators
from ui.pages.base_page import BasePage
# from ui.pages.main_page import MainPage


class CompanyPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = CompanyPageLocators

    def create_new_company(self, file_path):
        create_button = self.find(self.locators.CREATE_COMPANY_BUTTON_LOCATOR, 10)
        create_button.click()
        coverage_type_button = self.find(self.locators.TRAFFIC_BUTTON_LOCATOR, 10)
        coverage_type_button.click()
        url_field = self.find(self.locators.URL_COMPANY_FIELD_LOCATOR, 10)
        url_field.send_keys(self.url)
        banner_button = self.find(self.locators.BANNER_LOCATOR, 10)
        banner_button.click()
        upload_picture = self.find(self.locators.INPUT_PICT_LOCATOR, 10)
        upload_picture.send_keys(file_path)
        self.click(self.locators.BUTTON_SUBMIT_LOCATOR, 10)
