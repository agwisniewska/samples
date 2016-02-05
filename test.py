from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time, re


driver = webdriver.Firefox()

driver.get("http://www.google.pl")
assert "Google" in driver.title
pole = driver.find_element_by_id("lst-ib")
pole.send_keys("python")
button = driver.find_element_by_name("btnG")
button.click()
wait = WebDriverWait(driver, 3)
wait.until(lambda d : d.title.lower().startswith('python'))
assert "python" in driver.title
driver.close()