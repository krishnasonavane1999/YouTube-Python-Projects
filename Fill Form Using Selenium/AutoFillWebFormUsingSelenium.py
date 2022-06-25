from selenium import webdriver
from selenium.webdriver.common.by import By #pip install selenium
import time

chrome_webdriver_path = "<Your Chrome Driver Path> - chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_webdriver_path)

form_url = "Your Form URL"

driver.get(form_url)


first_name = driver.find_element(by=By.CSS_SELECTOR, value="<Selector value here>")
first_name.send_keys("Monica")
time.sleep(1)

last_name = driver.find_element(by=By.CSS_SELECTOR, value="<Selector value here>")
last_name.send_keys("Geller")
time.sleep(1)

where_from = driver.find_element(by=By.CSS_SELECTOR, value="<Selector value here>")
where_from.send_keys("New York")
time.sleep(1)

subscribed = driver.find_element(by=By.CSS_SELECTOR, value="<Selector value here>")
subscribed.click()
time.sleep(1)
just_subscribed = driver.find_element(by=By.CSS_SELECTOR, value="<Selector value here>")

time.sleep(2)

submit = driver.find_element(by=By.CSS_SELECTOR, value="<Selector value here>")
submit.click()

# selecting elements using other selectors
''''
# select using CSS selector
first_name = driver.find_element(by=By.CSS_SELECTOR, value="<Selector value here>")

# select using ID
first_name = driver.find_element(by=By.ID, value="<Selector value here>")

# select using ID
first_name = driver.find_element(by=By. <jaise hee aap . type karoge aapko availabel suggestions mil jayenge>, value="<Selector value here>")
'''