from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.google.com")
#assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

continue_link = driver.find_elements_by_link_text('')
print( "number of links={length}").format(length = len(continue_link))
#print ("bcd {number} rather").format(number = 3)

driver.close()