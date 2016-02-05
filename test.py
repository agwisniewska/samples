from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.google.pl")
assert Google in driver.title
pole = driver.find_element_by_id("lst-ib")
pole.send_keys("python")
pole.send_keys(Keys.Return)
assert Python in driver.title
driver.close()