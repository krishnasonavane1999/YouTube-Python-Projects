import time
from selenium import webdriver # pip install selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver_path = "Chrome Driver's complete Path here"

url = "Website url here"

chrome = webdriver.Chrome(executable_path=driver_path)
chrome.maximize_window()

action = ActionChains(chrome)

chrome.get(url)

heading = chrome.find_element(by=By.ID, value="element's ID here")

'''
heading = chrome.find_element(by=By.CSS_SELECTOR, value="element's Selector here")
heading = chrome.find_element(by=By.XPATH, value="element's XPATH here")
heading = chrome.find_element(by=By.CLASS_NAME, value="element's Class namehere")
...
'''

# mouse hover
action.move_to_element(to_element=heading)

# mouse left click
# action.click(on_element=heading)
# time.sleep(2)

# action.double_click()
# mouse right click
# action.context_click(on_element=heading)

action.perform()

# time.sleep(3)

#scroll page
chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")



