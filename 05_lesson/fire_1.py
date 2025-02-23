from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/entry_ad')
sleep(5)

driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

driver.quit()
