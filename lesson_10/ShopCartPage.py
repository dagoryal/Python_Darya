import allure
from selenium.webdriver.common.by import By

@allure.suite("Интернет-магазин")
class CartPage:
    def __init__(self, driver):
        self._driver = driver

    def get(self):
        with allure.step("Перейти в корзину"):
            self._driver.get('https://www.saucedemo.com/cart.html')
        with allure.step("Нажать кнопку Checkout"):
            self._driver.find_element(By.ID, 'checkout').click()
