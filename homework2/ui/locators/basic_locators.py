from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button-')]")
LOGIN_EMAIL_LOCATOR = (By.NAME, 'email')
LOGIN_PASSWORD_LOCATOR = (By.NAME, 'password')

FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//div[@class="input__wrap"]//input[@type="text"]')
PHONE_LOCATOR = (By.XPATH, '//div[@data-name="PHONE"]')
BUTTON_SAVE_LOCATOR = (By.XPATH, '//button[@data-class-name="Submit"]')
BILLING_CLASS_LOCATOR = (By.XPATH, '//div[contains(@class, "target-page")]')
STATISTICS_CLASS_LOCATOR = (By.XPATH, "//div[contains(@class, 'page_statistics')]")

class BasePageLocators:
    ACCOUNT_ACTIONS_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
    ACCOUNT_LOGOUT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')
    PROFILE_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
    BILLING_MENU_LOCATOR = (By.XPATH, '//a[@href="/billing"]')
    STATISTICS_MENU_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')

class MainPageLocators(BasePageLocators):
    LOGIN_DONE_PAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "layout-module-page-")]')




class SearchPageLocators(BasePageLocators):
    pass


class PythonEventsPageLocators(BasePageLocators):
    pass

