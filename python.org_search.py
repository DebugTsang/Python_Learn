# This program demo how to use selenium and grab all urls
# Loating elements
# http://selenium-python.readthedocs.org/en/latest/locating-elements.html
# Date: 2015-07-12 21:00

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("http://www.google.com")
#assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
wait = WebDriverWait(driver, 2)
continue_link = driver.find_elements_by_link_text('')
print continue_link[0].get_attribute("href");
print( "number of links={length}").format(length = len(continue_link))
driver.close()