from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InfoPage:
    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')


    def info(self):
        self._driver.find_element(By.ID, 'first-name').send_keys('Darya')
        self._driver.find_element(By.ID, 'last-name').send_keys('Gorchakova')
        self._driver.find_element(By.ID, 'postal-code').send_keys('123456')
        self._driver.find_element(By.ID, 'continue').click()

    def total(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label')))
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label')
        return total.text
