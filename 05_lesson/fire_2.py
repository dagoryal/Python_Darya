from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/inputs')

search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
search_input.send_keys('1000', Keys.RETURN)

sleep(3)

search_input.clear()
search_input.send_keys('999', Keys.RETURN)

sleep(2)
driver.quit()
