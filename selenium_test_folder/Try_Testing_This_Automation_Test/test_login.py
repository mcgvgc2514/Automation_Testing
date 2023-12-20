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
    login_page.verify_double_click_text()
    login_page.verify_double_click_button()

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("test")
    login_page.enter_password("test")
    login_page.click_login()
    login_page.verify_login_success()
    
def test_login_failure_accept(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("faI1l")
    login_page.enter_password("faI1l")
    login_page.click_login()
    login_page.click_accept_alert()

def test_login_failure_dismiss(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("faI1l")
    login_page.enter_password("faI1l")
    login_page.click_login()
    login_page.click_dismiss_alert()

def test_sample_alert_accept(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.click_sample_alert_button()
    login_page.click_accept_alert()
    login_page.verify_sample_alert_after_press("You Pressed the OK Button!")

def test_sample_alert_dismiss(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.click_sample_alert_button()
    login_page.click_dismiss_alert()
    login_page.verify_sample_alert_after_press("You pressed the Cancel Button!")

def test_sample_photo(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.verify_sample_photo_text()
    login_page.verify_sample_photo_image()
    login_page.verify_sample_photo_description()

def test_tool_tip(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.hover_sample_tooltip()
    login_page.verify_tool_tip_text()
