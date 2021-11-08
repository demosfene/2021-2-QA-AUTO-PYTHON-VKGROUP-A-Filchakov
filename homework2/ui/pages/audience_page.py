import uuid

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from ui.locators.basic_locators import AudiencePageLocators
from ui.pages.base_page import BasePage


class AudiencePage(BasePage):
    locators = AudiencePageLocators
    url = 'https://target.my.com/segments/segments_list'

    def create_new_segment(self):
        self.find(self.locators.CREATE_NEW_SEGMENT_LOCATOR, 10)
        id_segment = None
        try:
            self.click(self.locators.CREATE_NEW_SEGMENT_LOCATOR, 5)
        except TimeoutException:
            self.click(self.locators.CREATE_FIRST_SEGMENT_LOCATOR, 5)

        self.click(self.locators.ITEM_SEGMENT_LOCATOR, 5)
        self.click(self.locators.CHECKBOX_LOCATOR, 5)
        self.click(self.locators.ADD_SEGMENT_LOCATOR, 5)
        name_field = self.find(self.locators.NAME_SEGMENT_LOCATOR, 10)
        name = uuid.uuid4()
        name_field.clear()
        name_field.send_keys(str(name))
        self.click(self.locators.CREATE_SEGMENT_LOCATOR, 5)
        self.find(self.locators.SEGMENT_ELEMENTS_LOCATOR, 10)
        segments_elems = self.driver.find_elements_by_xpath(xpath=self.locators.SEGMENT_ELEMENTS_LOCATOR[1])
        for i, elem in enumerate(segments_elems):
            if str(name) == str(elem.text):
                id_segment = segments_elems[i - 1].text
                break
        return id_segment

    def remove_segment(self, id_segment):
        LOCATOR = (By.XPATH, '//div[contains(@data-test, "remove-'+id_segment+'")]')
        remove_field = self.find(LOCATOR, 10)
        remove_field.click()
        try:
            return self.find(LOCATOR, 10)
        except TimeoutException:
            return True
