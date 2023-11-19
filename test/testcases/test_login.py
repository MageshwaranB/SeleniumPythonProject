import logging

import pytest
from selenium import webdriver
from src.page_objects.login_page import LoginPage
from src.utilities.read_properties import ReadConfig
from src.utilities.custom_logs import LogGen


class TestLogin:
    logger = LogGen.generate_logs()

    def test_login_page(self, setup):

        self.logger.info("Staring the test - TestLogin")
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.logger.info("Entering the email and password")
        self.login_page.set_username(ReadConfig.get_username())
        self.login_page.set_password(ReadConfig.get_password())
        self.logger.info("Clicking the login button")
        actual = self.login_page.click_login_button()

        if actual == 'Dashboard / nopCommerce administration':
            self.driver.close()
            self.logger.info("Testcase is passed")
            assert True

        else:
            self.driver.save_screenshot("src/Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.error("Testcase is failed")
            assert False
