from selenium import webdriver
import pytest
from src.utilities.read_properties import ReadConfig


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(ReadConfig.get_application_url())
    # yield driver.close()
    return driver
