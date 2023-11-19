from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        email_field = self.driver.find_element(By.ID, self.textbox_email_id)
        email_field.clear()
        email_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element(By.ID, self.textbox_password_id)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        return self.driver.title
