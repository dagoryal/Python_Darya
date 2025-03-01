import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')

def test_shop():
#Авторизоваться
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')

    passw = driver.find_element(By.ID, 'password')
    passw.send_keys('secret_sauce')

    driver.find_element(By.ID, 'login-button').click()
    wait =WebDriverWait(driver, 10)

#Добавить товары в корзину
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))
    ).click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

#Перейти в корзину

    driver.find_element(By.ID, 'shopping_cart_container').click()

#Нажать чекаут

    driver.find_element(By.ID, 'checkout').click()

#Заполнить форму данными
    driver.find_element(By.ID, 'first-name').send_keys('Darya')
    driver.find_element(By.ID, 'last-name').send_keys('Gorchakova')
    driver.find_element(By.ID, 'postal-code').send_keys('123456')
    driver.find_element(By.ID, 'continue').click()

#Итоговая стоимость
    total = (wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label')))
             .text)

    driver.quit()

    assert total == 'Total: $58.29'
