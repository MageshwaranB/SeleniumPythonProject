import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

def test_launch_browser(setup):
    setup.get("https://www.google.com/")
    current_url = setup.current_url
    setup.save_screenshot("")

