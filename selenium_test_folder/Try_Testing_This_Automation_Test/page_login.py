from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "uname")
        self.password_textbox = (By.ID, "pwd")
        self.login_button = (By.XPATH, "//input[@value='Login']")


    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    def verify_success(self):
        assert "Successful" in self.driver.page_source

    def click_accept_alert(self):
        Alert(self.driver).accept()

    def click_dismiss_alert(self):
        Alert(self.driver).dismiss()

    def click_sample_alert_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/button").click()