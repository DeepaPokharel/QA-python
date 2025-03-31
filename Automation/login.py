# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time
from selenium.webdriver.common.by import By

# Driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# website selection
# url = "https://www.saucedemo.com"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(url)
driver.maximize_window()  
time.sleep(5)     #maximize the browser window
title = driver.title
print(title)

# username = driver.find_element(By.ID, "user-name")
# username.send_keys("standard_user")
# time.sleep(3)

# password = driver.find_element(By.ID, "password")
# password.send_keys("secret_sauce")
# time.sleep(3)


# login_button = driver.find_element(By.ID, "login-button")
# login_button.click()
# time.sleep(4)

# username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
# username.send_keys("standard_user")
# time.sleep(3)


# password = driver.find_element(By.NAME, "password")
# password.send_keys("secret_sauce")
# time.sleep(3)


# login_button = driver.find_element(By.NAME, "login-button")
# login_button.click()
# time.sleep(4)

# title = driver.current_url
# if (title == "https://www.saucedemo.com/v1/inventory.html"):
#     print("Login is successful")
# else:
#     print("Login is unsuccessful")

username = driver.find_element(By.XPATH,"//input[@placeholder='Username']")
username.send_keys("Admin")
time.sleep(3)

password = driver.find_element(By.NAME,'password')
password.send_keys("admin123")
time.sleep(3)


login_button = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
login_button.click()
time.sleep(4)

title = driver.current_url
if (title == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
    print("Login is successful")
else:
    print("Login is unsuccessful")

driver.quit()
