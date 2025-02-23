from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")

    but = WebDriverWait(driver, 10).until(element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))

    sleep(5)


'''это еще вариант, не знаю так ли надо было. '''
# for i in range(3):
#     but = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
#     but.click()

# sleep(5)


# driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

# sleep(5)
