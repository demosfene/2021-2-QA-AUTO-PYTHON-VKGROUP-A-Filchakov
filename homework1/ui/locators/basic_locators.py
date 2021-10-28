from selenium.webdriver.common.by import By

QUERY_LOCATOR = (By.ID, 'id-search-field')
GO_LOCATOR = (By.ID, 'submit')
LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button-')]")
LOGIN_EMAIL_LOCATOR = (By.NAME, 'email')
LOGIN_PASSWORD_LOCATOR = (By.NAME, 'password')
LOGIN_DONE_PAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "layout-module-page-")]')
ACCOUNT_ACTIONS_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
ACCOUNT_LOGOUT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')
MAIN_PAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "mainPage-module-page")]')
PROFILE_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//div[@class="input__wrap"]//input[@type="text"]')
PHONE_LOCATOR = (By.XPATH, '//div[@data-name="PHONE"]')
BUTTON_SAVE_LOCATOR = (By.XPATH, '//button[@data-class-name="Submit"]')
BILLING_MENU_LOCATOR = (By.XPATH, '//a[@href="/billing"]')
BILLING_CLASS_LOCATOR = (By.XPATH, '//div[contains(@class, "target-page")]')
STATISTICS_MENU_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')
STATISTICS_CLASS_LOCATOR = (By.XPATH, "//div[contains(@class, 'page_statistics')]")
