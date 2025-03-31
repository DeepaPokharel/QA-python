from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome  import ChromeDriverManager

# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft  import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox  import GeckoDriverManager

import time

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# url = "https://google.com"
url = "https://merolagani.com"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(5)

driver.quit()