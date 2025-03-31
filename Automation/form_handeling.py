from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://formy-project.herokuapp.com/form"

driver.get(url)
driver.maximize_window()       #maximize the browser window
title = driver.title
print(title)


Firstname = driver.find_element(By.XPATH,"//input[@id='first-name']")
Firstname.send_keys("Ani")
time.sleep(3)

Lastname = driver.find_element(By.XPATH,"//input[@id='last-name']")
Lastname.send_keys("Doe")
time.sleep(3)


Job_Title = driver.find_element(By.XPATH,"//input[@id='job-title']")
Job_Title.send_keys("QA")
time.sleep(3)

Education= driver.find_element(By.XPATH,"//input[@id='radio-button-1']")
Education.click()
time.sleep(2)


driver.execute_script("window.scrollBy(0,400);")

Gender= driver.find_element(By.XPATH,"//input[@id='checkbox-3']")
Gender.click()
time.sleep(2)


Experience = driver.find_element(By.XPATH,"//select[@id='select-menu']")
Experience.click()
time.sleep(2)

year_select = driver.find_element(By.XPATH,'//*[@id="select-menu"]')
year_select.click()
time.sleep(2)

date_picker = driver.find_element(By.XPATH,'//*[@id="datepicker"]')
date_picker.send_keys("03/11/2025")
time.sleep(2)

submit_button = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/form[1]/div[1]/div[8]/a[1]')
submit_button.click()
time.sleep(2)

# links = driver.find_elements(By.TAG_NAME,"a")
# print(len(links))

title = driver.current_url
if (title == "https://formy-project.herokuapp.com/thanks"):
    print("submission is successful")
else:
    print("Submission is unsuccessful")

driver.quit()
