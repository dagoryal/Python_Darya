import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@allure.suite("Интернет-магазин")
class Shop:
    @allure.step("Открыть сайт магазина")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    @allure.step("Авторизоваться")
    def authorization(self):
        self._driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self._driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self._driver.find_element(By.ID, 'login-button').click()
        WebDriverWait(self._driver, 10)

    @allure.step("Добавить в корзину товары")
    def buy_item(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
