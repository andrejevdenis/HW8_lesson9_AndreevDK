import time

import pytest
from selene import browser, have, be
from selenium import webdriver

@pytest.fixture()
def browser_management():
    # driver_options = webdriver.FirefoxOptions()
    # #driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options
    # browser.config.driver_name = 'firefox'
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.fullscreen_window()

    yield

    browser.with_(time.sleep(5)).quit()