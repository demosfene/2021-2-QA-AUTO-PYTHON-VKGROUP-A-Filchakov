import os
import time
from contextlib import contextmanager

import allure
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base import BaseCase
from ui.locators import basic_locators
import pytest

from utils.decorators import wait


class TestOne(BaseCase):

    def test_title(self):
        assert "Python" in self.driver.title

    def test_relative(self):
        introduction = self.main_page.find(self.main_page.locators.INTRODUCTION)
        learn_more = introduction.find_element(*self.main_page.locators.LEARN_MORE_RELATIVE)
        assert learn_more.get_attribute('href') == self.driver.current_url + 'doc/'


class TestLoad(BaseCase):

    def check_download(self, temp_dir, file_name):
        if selenoid := self.config['selenoid']:
            res = requests.get(f'{selenoid}/download/{self.driver.session_id}/{file_name}')
            if res.status_code == 404:
                return False

            with open(os.path.join(temp_dir, file_name), 'wb') as f:
                f.write(res.content)
            return True

        else:

            for f in os.listdir(temp_dir):
                if f.endswith('.crdownload'):
                    return False

            assert file_name in os.listdir(temp_dir)
            return True

    def test_download(self, temp_dir):
        from selenium.webdriver.common.by import By
        self.driver.get('https://www.python.org/downloads/release/python-2717/')

        file_name = 'python-2.7.17.amd64-pdb.zip'
        self.main_page.click((By.XPATH, f'//a[contains(@href, "{file_name}")]'))

        wait(self.check_download, error=AssertionError, check=True, temp_dir=temp_dir, file_name=file_name)

    @pytest.fixture()
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'files', 'userdata')

    def test_upload(self, file_path):
        from selenium.webdriver.common.by import By
        self.driver.get('https://ps.uci.edu/~franklin/doc/file_upload.html')
        locator = (By.NAME, 'userfile')

        input_field = self.main_page.find(locator)
        time.sleep(5)
        input_field.send_keys(file_path)
        time.sleep(5)


class TestIframe(BaseCase):

    def test_iframe(self):
        self.main_page.click(self.main_page.locators.START_SHELL)
        time.sleep(5)

        console_iframe = self.main_page.find(self.main_page.locators.CONSOLE_IFRAME)
        self.driver.switch_to.frame(console_iframe)

        input_iframe = self.main_page.find(self.main_page.locators.INPUT_IFRAME)
        self.driver.switch_to.frame(input_iframe)

        iframe = self.main_page.find((By.XPATH, '//iframe'))
        self.driver.switch_to.frame(iframe)

        console = self.main_page.find(self.main_page.locators.PYTHON_CONSOLE)
        console.send_keys('assert 1 == 0')
        console.send_keys(Keys.RETURN)

        time.sleep(10)

        self.driver.switch_to.default_content()

    @contextmanager
    def switch_to_next_windows(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    def test_new_tab(self):
        current_window = self.driver.current_window_handle

        events_button = self.main_page.find(self.main_page.locators.EVENTS_BUTTON)
        self.main_page.action_chains.key_down(Keys.COMMAND).click(events_button).key_up(Keys.COMMAND).perform()

        with self.switch_to_next_windows(current_window, close=True):
            assert self.driver.current_url == 'https://www.python.org/events/'



class TestFailure(BaseCase):

    @allure.epic('Awesome PyTest framework')
    @allure.feature('UI tests')
    @allure.story('Failure tests')
    def test_failure(self):
        self.main_page.find((By.XPATH, '32132183789127389217'), timeout=1)

    @allure.epic('Awesome PyTest framework')
    @allure.feature('UI tests')
    @allure.story('Failure tests')
    def test_failure_log(self):
        self.driver.get('https://target.my.com/')
        time.sleep(1)
        assert 0


class TestLog(BaseCase):

    @allure.epic('Awesome PyTest framework')
    @allure.feature('UI tests')
    @allure.story('Log tests')
    @allure.testcase('Python events')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.issue('https://jira.vk.team/ISSUE-123')
    @allure.description("""We just go to python.org, then we go to events, then we go to PyConTW 2021 and then check
    it's location. Hmmm... Sounds good. Lois.
        """)
    @pytest.mark.smoke
    def test_log(self):
        self.logger.info('Ready to go to python-events')

        with allure.step('Going to python-events'):
            python_events_page = self.main_page.go_to_events('python-events')

        self.logger.info('Going to PyConTW 2021 event')
        python_events_page.click(python_events_page.locators.PYCONTW_2021)
        location = python_events_page.get_location()

        self.logger.info(f'Got PyConTW 2021 location: {location}')
        with allure.step(f'Checking location == "{location}"'):
            assert location == "Online"


@pytest.mark.skip("SKIP")
def test_all_browsers(all_drivers):
    time.sleep(2)
