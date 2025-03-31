from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://demo.nopcommerce.com/register"

driver.get(url)
driver.maximize_window()       #maximize the browser window
title = driver.title
print(title)


driver.execute_script("window.scrollBy(0,300);")
# is_dispalyed & is_enabled

# Search = driver.find_element(*(By.XPATH,"//input[@id='small-searchterms']"))
# print("displayed status:", Search.is_displayed())
# print("enabled status:", Search.is_enabled())

# is_selected-- for radio button & checkboxes

Gender = driver.find_element(*(By.XPATH,"//label[normalize-space()='Female']"))
Gender.click()
time.sleep(2)

Firstname= driver.find_element(*(By.XPATH,"//input[@id='FirstName']"))
Firstname.send_keys("Deepa")
time.sleep(2)

Lastname = driver.find_element(*(By.XPATH,"//input[@id='LastName']"))
Lastname.send_keys("Khanal")
time.sleep(2)

Email = driver.find_element(*(By.XPATH,"//input[@id='Email']"))
Email.send_keys("abcd123@gmail.com")
time.sleep(2)


driver.quit()
