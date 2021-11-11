from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCOUNT_ACTIONS_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
    ACCOUNT_LOGOUT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')
    PROFILE_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
    BILLING_MENU_LOCATOR = (By.XPATH, '//a[@href="/billing"]')
    STATISTICS_MENU_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')
    CAMPAIGN_PAGE_LOCATOR = (By.XPATH, '//a[@href="/dashboard"]')
    AUDIENCE_PAGE_LOCATOR = (By.XPATH, '//a[@href="/segments"]')


class LoginPageLocators:
    LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    LOGIN_EMAIL_LOCATOR = (By.NAME, 'email')
    LOGIN_PASSWORD_LOCATOR = (By.NAME, 'password')
    NOTIFY_ERROR_LOCATOR = (By.XPATH, "//div[contains(@class, 'notify-module-error')]")


class MainPageLocators(BasePageLocators):
    LOGIN_DONE_PAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "layout-module-page")]')


class AudiencePageLocators(MainPageLocators):
    CREATE_FIRST_SEGMENT_LOCATOR = (By.XPATH, '//a[contains(@href, "/segments/segments_list/new/"]')
    CREATE_NEW_SEGMENT_LOCATOR = (By.XPATH, '//button[contains(@class, "button_submit")]')
    ITEM_SEGMENT_LOCATOR = (By.XPATH, '//div[contains(@class, "adding-segments-item_active")]')
    CHECKBOX_LOCATOR = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    ADD_SEGMENT_LOCATOR = (By.XPATH, '//div[contains(@class, "adding-segments-modal__btn-wrap")]')
    CREATE_SEGMENT_LOCATOR = (By.XPATH, '//div[contains(@class, "create-segment-form__btn-wrap")]'
                                        '//button[contains(@class,"button_submit")]')
    NAME_SEGMENT_LOCATOR = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]'
                                      '//div[contains(@class, "input__wrap")]'
                                      '//input[contains(@class, input__inp)]')
    SEGMENT_ELEMENTS_LOCATOR = (By.XPATH, '//div[contains(@class, "main-module-Cell")]')


class CampaignPageLocators(MainPageLocators):
    CREATE_CAMPAIGN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]'
                                               '//div[contains(@class, "button-module-button")]')
    TRAFFIC_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')
    URL_CAMPAIGN_FIELD_LOCATOR = (By.XPATH, '//input[contains(@class, "mainUrl-module-searchInput")]')
    CAMPAIGN_NAME_FIELD_LOCATOR = (By.XPATH, '//div[contains(@class, "campaign-name__name-wrap")]'
                                            '//div[contains(@class, "input_campaign-name")]'
                                            '//div[contains(@class, "input__wrap")]'
                                            '//input[@type = "text"]')
    BANNER_LOCATOR = (By.XPATH, '//div[@id = "patterns_banner_4"]')
    INPUT_PICT_LOCATOR = (By.XPATH, '//div[contains(@class, "bannerForm-module-fieldsWrapForInline")]'
                                    '//div[contains(@class, "bannerForm-module-roleInline")]'
                                    '//div[contains(@class, "roles-module-item")]'
                                    '//div[contains(@class, "roles-module-buttonWrap")]'
                                    '//div[contains(@class, "upload-module-wrapper")]'
                                    '/input[1]')

    BUTTON_SUBMIT_LOCATOR = (By.XPATH, '//div[contains(@class, "footer__controls-wrap")]'
                                       '//div[contains(@class, "footer__buttons-wrap")]'
                                       '//div[contains(@class, "footer__button")]'
                                       '//button[contains(@class, "button_submit")]')

    NOTIFY_SUCCESS_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, '//div[contains(@class, "group-module-group")]'
                                                       '//div[contains(@class, "group-module-item")]')

    def SETTINGS_BY_ID_LOCATOR(campaign_id):
        return By.XPATH, f'//div[contains(@class, "main-module-Cell") and contains(@data-test, "setting-{campaign_id}")]' \
                         '//div[contains(@class,"settingsCell-module-settingsCellWrap")]'
