import logging

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from homework2.ui.pages.base_page import BasePage
from homework2.ui.pages.main_page import MainPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


def get_driver(config, download_dir=None):
    browser_name = config['browser']
    selenoid = config['selenoid']
    vnc = config['vnc']

    if browser_name == 'chrome':
        options = Options()
        if download_dir is not None:
            options.add_experimental_option("prefs", {"download.default_directory": download_dir})

        if selenoid:
            options.add_experimental_option("prefs", {"download.default_directory": '/home/selenium/Downloads'})
            capabilities = {
                'browserName': 'chrome',
                'version': '89.0'
            }
            if vnc:
                capabilities['version'] += '_vnc'
                capabilities['enableVNC'] = True

            browser = webdriver.Remote(selenoid, options=options,
                                       desired_capabilities=capabilities)
        else:
            manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
            browser = webdriver.Chrome(executable_path=manager.install(), options=options)

    elif browser_name == 'firefox':
        manager = GeckoDriverManager(version='latest')
        browser = webdriver.Firefox(executable_path=manager.install())
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = config['url']
    with allure.step('Init browser'):
        browser = get_driver(config, download_dir=temp_dir)
        browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    config['browser'] = request.param

    browser = get_driver(config)
    browser.get(url)
    yield browser
    browser.quit()

