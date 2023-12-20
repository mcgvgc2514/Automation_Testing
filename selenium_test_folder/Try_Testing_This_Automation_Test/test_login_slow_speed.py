# Navigate to folder in terminal and type "pytest {filename}.py" to run
# Run tests by keyword: pytest -k {keyword}
# To add test results, add "--html=reports" to the end of terminal command

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager
from pages import LoginPage


# Use fixture() to create setup and teardown for test cases:
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_double_click(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.verify_double_click_text()
    time.sleep(1)
    login_page.verify_double_click_button()
    time.sleep(1)

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.enter_username("test")
    time.sleep(1)
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    login_page.verify_login_success()
    time.sleep(1)
    
def test_login_failure_accept(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.enter_username("faI1l")
    time.sleep(1)
    login_page.enter_password("faI1l")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    login_page.click_accept_alert()
    time.sleep(1)

def test_login_failure_dismiss(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.enter_username("faI1l")
    time.sleep(1)
    login_page.enter_password("faI1l")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    login_page.click_dismiss_alert()
    time.sleep(1)

def test_sample_alert_accept(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.click_sample_alert_button()
    time.sleep(1)
    login_page.click_accept_alert()
    time.sleep(1)
    login_page.verify_sample_alert_after_press("You Pressed the OK Button!")
    time.sleep(1)

def test_sample_alert_dismiss(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.click_sample_alert_button()
    time.sleep(1)
    login_page.click_dismiss_alert()
    time.sleep(1)
    login_page.verify_sample_alert_after_press("You pressed the Cancel Button!")
    time.sleep(1)

def test_sample_photo(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.verify_sample_photo_text()
    time.sleep(1)
    login_page.verify_sample_photo_image()
    time.sleep(1)
    login_page.verify_sample_photo_description()
    time.sleep(1)

def test_tool_tip(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    time.sleep(1)
    login_page.hover_sample_tooltip()
    time.sleep(1)
    login_page.verify_tool_tip_text()
    time.sleep(1)
