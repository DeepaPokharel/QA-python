# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager
import pytest
import time

@pytest.fixture(scope = "module")

def browser(): #initialization for browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_website(browser):
    url = "https://google.com"
    browser.get(url)
    browser.maximize_window()
    assert "YouTube" in browser.title, f"Expected YouTube but got '{browser.title}'"
    time.sleep(3)