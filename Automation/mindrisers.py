# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time
from selenium.webdriver.common.by import By

# Driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# website selection
url = "https://www.mindrisers.com.np/online-admission"

driver.get(url)
driver.maximize_window()       #maximize the browser window
title = driver.title
print(title)


driver.execute_script("window.scrollBy(0,900);")

Fullname = driver.find_element(By.XPATH,"//input[@id='full_name']")
Fullname.send_keys("Binita")
time.sleep(3)


Email = driver.find_element(By.XPATH,"//input[@id='email']")
Email.send_keys("Apple0000@gmail.com")
time.sleep(3)

College_name = driver.find_element(By.XPATH,"//input[@id='college']")
College_name.send_keys("Nepathya")
time.sleep(3)


phone = driver.find_element(By.XPATH,"//input[@id='mobile_no']")
phone.send_keys("9867452921")
time.sleep(3)


Academic_Status = driver.find_element(By.XPATH,"//select[@id='qualification']")
Academic_Status.click()
time.sleep(3)

Complete_education = driver.find_element(By.XPATH,'//*[@id="qualification"]/option[2]')
Complete_education.click()
time.sleep(2)

Course = driver.find_element(By.XPATH,"//select[@id='course']")
Course.click()
time.sleep(3)

Interested_Course= driver.find_element(By.XPATH,'//*[@id="course"]/option[5]')
Interested_Course.click()
time.sleep(2)

Class_schedule = driver.find_element(By.XPATH,"//select[@id='shedule']")
Class_schedule.click()
time.sleep(3)

Preferred_schedule = driver.find_element(By.XPATH,'//*[@id="shedule"]/option[2]')
Preferred_schedule.click()
time.sleep(2)


# driver.execute_script("window.scrollBy(0,400);")

Internship_program = driver.find_element(By.XPATH,"//input[@id='remarks-yes']")
Internship_program.click()
Internship_program.click()
time.sleep(3)

Queries = driver.find_element(By.XPATH,"//textarea[@id='question']")
Queries.send_keys("no")
time.sleep(3)

driver.quit()