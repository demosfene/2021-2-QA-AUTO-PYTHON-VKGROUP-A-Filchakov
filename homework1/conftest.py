import pytest
from selenium import webdriver
from base import config


@pytest.fixture(scope='function')
def driver():
    browser_path = config['Driver']['browser_path']
    main_url = config['Tests']['main_url']

    browser = webdriver.Chrome(executable_path=browser_path)
    browser.maximize_window()
    browser.get(main_url)

    yield browser
    browser.close()
