import allure

from homework2.ui.locators.basic_locators import MainPageLocators
from homework2.ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()
