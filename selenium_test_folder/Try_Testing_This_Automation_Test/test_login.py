# Navigate to folder in terminal and type "pytest {filename}.py" to run
# Run tests by keyword: pytest -k {keyword}
# To add test results, add "--html=reports" to the end of terminal command

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from login_page import LoginPage
from selenium.webdriver.common.alert import Alert


# Use fixture() to create setup and teardown for test cases:
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_username("test")
    time.sleep(1)
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    login_page.verify_success()
    time.sleep(1)
    
def test_login_failure_accept(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_username("faI1l")
    time.sleep(1)
    login_page.enter_password("faI1l")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    login_page.click_accept_alert()

def test_login_failure_dismiss(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_username("faI1l")
    time.sleep(1)
    login_page.enter_password("faI1l")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    login_page.click_dismiss_alert()

def test_sample_alert(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.click_sample_alert_button()
    time.sleep(1)
    login_page.click_dismiss_alert()