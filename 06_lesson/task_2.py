from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('http://uitestingplayground.com/textinput')

but_txt = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
but_txt.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

new_but = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(new_but)

driver.quit()