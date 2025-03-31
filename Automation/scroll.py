# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time

# Driver installation
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# website selection
url = "https://merolagani.com"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)

# page_height =driver.execute_script("return document.body.scrollHeight")
# scroll_speed = 300
# scroll_iteration = int(page_height/scroll_speed)

# for _ in range(scroll_iteration):
#     driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
#     time.sleep(2)

driver.execute_script("window.scrollBy(0,300);")

time.sleep(5)

driver.quit()