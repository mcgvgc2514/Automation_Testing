from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        # Declare driver variable here:
        self.driver = driver
        self.login_page_url = "https://trytestingthis.netlify.app/"
        # Declare variables that locate certain elements on the page:
        self.loc_username_textbox = (By.ID, "uname")
        self.loc_password_textbox = (By.ID, "pwd")
        self.loc_login_button = (By.XPATH, "//input[@value='Login']")
        self.loc_sample_alert_button = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/button")
        self.loc_sample_alert_button_after_press = (By.ID, "demo")
        self.loc_sample_photo_text = (By.XPATH, "/html/body/div[3]/div[1]/h4")
        self.loc_sample_photo_image = (By.XPATH, "/html/body/div[3]/div[1]/div[3]")
        self.loc_sample_photo_description = (By.XPATH, "/html/body/div[3]/div[1]/p[1]")
        self.loc_sample_photo_emojis = (By.XPATH, "/html/body/div[3]/div[1]/p[2]")
        self.loc_sample_tooltip = (By.XPATH, "/html/body/div[3]/div[1]/div[2]")
        self.loc_sample_tooltip_txt = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/span")


    def click_accept_alert(self):
        Alert(self.driver).accept()

    def click_dismiss_alert(self):
        Alert(self.driver).dismiss()

    def click_login(self):
        self.driver.find_element(*self.loc_login_button).click()

    def click_sample_alert_button(self):
        self.driver.find_element(*self.loc_sample_alert_button).click()

    def enter_password(self, password):
        self.driver.find_element(*self.loc_password_textbox).send_keys(password)

    def enter_username(self, username):
        self.driver.find_element(*self.loc_username_textbox).send_keys(username)
        
    def hover_sample_tooltip(self):
        self.sample_tooltip = self.driver.find_element(*self.loc_sample_tooltip)
        ActionChains(self.driver).move_to_element(self.sample_tooltip).perform()
 
    def open_login_page(self):
        self.driver.get(self.login_page_url)
        self.driver.maximize_window()

    def verify_sample_alert_after_press(self, text):
        self.sample_alert_button_after_press = self.driver.find_element(*self.loc_sample_alert_button_after_press)
        assert text in self.sample_alert_button_after_press.text

    def verify_success(self):
        assert "Successful" in self.driver.page_source

    def verify_sample_photo_description(self):
        self.sample_photo_description = self.driver.find_element(*self.loc_sample_photo_description)
        assert "This is your description of the photo" in self.sample_photo_description.text

    def verify_sample_photo_image(self):
        self.sample_photo_image = self.driver.find_element(*self.loc_sample_photo_image)

    def verify_sample_photo_text(self):
        self.sample_photo_text = self.driver.find_element(*self.loc_sample_photo_text)
        assert "This is your sample photo" in self.sample_photo_text.text

    def verify_tool_tip_text(self):
        self.sample_tooltip_txt = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.loc_sample_tooltip_txt))
        assert "This is your sample Tooltip text" in self.sample_tooltip_txt.text