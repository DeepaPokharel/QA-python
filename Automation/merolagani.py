from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


url = "https://merolagani.com/"

driver.get(url)
driver.maximize_window()       #maximize the browser window
title = driver.title
print(title)


market_field = driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market_field.click()
time.sleep(2)

alert= Alert(driver)
alert.dismiss()
time.sleep(2)

Live_Trading = driver.find_element(*(By.XPATH,"//a[normalize-space()='Live Trading']"))
Live_Trading.click()
time.sleep(2)

# driver.execute_script("window.open('about:blank', '_blank');")
# time.sleep(2)
driver.execute_script("window.scrollBy(0,400);")
time.sleep(3)

Barun = driver.find_element(*(By.XPATH,"//a[normalize-space()='BARUN']"))
Barun.click()
time.sleep(4)

driver.switch_to.window(driver.window_handles[1])

driver.execute_script("window.scrollBy(0,900);")

Price_History = driver.find_element(*(By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']"))
Price_History.click()
time.sleep(2)

Date_picker = driver.find_element(*(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']"))
Date_picker.send_keys("03/16/2025")
time.sleep(2)

Search_button = driver.find_element(*(By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lbtnSearchPriceHistory']"))
Search_button.click()
time.sleep(2)

driver.quit()