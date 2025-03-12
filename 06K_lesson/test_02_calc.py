import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

def test_calc():
    driver.find_element(By.ID, 'delay').clear()
    sec = (driver.find_element(By.ID, 'delay')
       .send_keys('45'))
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    wait = WebDriverWait(driver, 45)
    res = wait.until(
        EC.text_to_be_present_in_element ((By.CSS_SELECTOR, 'div.screen'),'15')
    )
    fin_res = driver.find_element(By.CSS_SELECTOR, 'div.screen').text

    assert fin_res == "15"

    driver.quit()
