import allure
from selenium.webdriver.common.by import By

@allure.suite("Интернет-магазин")
class CartPage:
    """
    Этот класс содержит в себе методы перехода в корзину.
    Нажатие кнопки "Checkout".
    """
    def __init__(self, driver):
        self._driver = driver

    def get(self) -> None:
        """
        Эта функция осуществляет переход в корзину.
        Нажатие кнопки Checkout.
        """
        with allure.step("Перейти в корзину"):
            self._driver.get('https://www.saucedemo.com/cart.html')
        with allure.step("Нажать кнопку Checkout"):
            self._driver.find_element(By.ID, 'checkout').click()
