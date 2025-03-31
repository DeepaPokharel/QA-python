from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://filebin.net/"

driver.get(url)
driver.maximize_window()       #maximize the browser window
title = driver.title


upload = driver.find_element(*(By.XPATH,"//input[@id='fileField']"))
upload.send_keys("C:/Users/deepa/Pictures/Camera Roll/8f36f464-c183-4e70-8867-d4680b493110 (1).jpeg")
time.sleep(2)

more_click= driver.find_element(*(By.XPATH,"//a[@id='dropdownFileMenuButton']"))
more_click.click()
time.sleep(3)

download = driver.find_element(*(By.XPATH,"//a[normalize-space()='Download file']"))
download.click()
time.sleep(3)

driver.quit()
