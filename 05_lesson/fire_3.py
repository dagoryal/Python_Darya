from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/login')

user_name = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
user_name.send_keys('tomsmith')

passw = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
passw.send_keys('SuperSecretPassword!')

sleep(2)

log = driver.find_element(By.CSS_SELECTOR, 'button')
log.click()

sleep(3)

driver.quit()
