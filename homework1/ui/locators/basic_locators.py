from selenium.webdriver.common.by import By

QUERY_LOCATOR = (By.ID, 'id-search-field')
GO_LOCATOR = (By.ID, 'submit')
LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button-')]")
LOGIN_EMAIL_LOCATOR = (By.NAME, 'email')
LOGIN_PASSWORD_LOCATOR = (By.NAME, 'password')
ACCOUNT_ACTIONS_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
ACCOUNT_LOGOUT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')
PROFILE_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//div[@class="input__wrap"]//input[@type="text"]')
PHONE_LOCATOR = (By.XPATH, '//div[@data-name="PHONE"]')
BUTTON_SAVE_LOCATOR = (By.XPATH, '//button[@data-class-name="Submit"]')
BILLING_LOCATOR = (By.XPATH, '//a[@href="/billing"]')
STATISTICS_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')

