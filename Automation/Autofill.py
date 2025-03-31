from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager

import time
import random
import string
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.mindrisers.com.np/contact-us"

driver.get(url)
driver.maximize_window()       #maximize the browser window
time.sleep(3)
driver.execute_script("window.scrollBy(0, 700);")
time.sleep(2)

title = driver.title
print(title)

name_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
Phone_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
Subject_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
Queries_field = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))

# Autofill generation
def generate_email():
    domain = "abc.com"
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def generate_name():
    return ''.join(random.choices(string.ascii_letters,k = 8))

def generate_phone():
    return "+977-98" + ''.join(random.choices(string.digits,k = 8))


def generate_subject():
    return ''.join(random.choices(string.ascii_letters, k= 30 ))

def generate_queries():
    return ''.join(random.choices(string.ascii_letters, k = 100))

# call function
name = generate_name()
email = generate_email()
phone = generate_phone()
subject= generate_subject()
queries = generate_queries()

# valve input(if there is default input in name field)
name_field.clear()

name_field.send_keys(name)
time.sleep(2)

email_field.send_keys(email)
time.sleep(2)

Phone_field.send_keys(phone)
time.sleep(2)

Subject_field.send_keys(subject)
time.sleep(2)

Queries_field.send_keys(queries)
time.sleep(2)