from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.find_element(By.ID, 'checkout').click()