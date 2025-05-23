import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@allure.suite("Интернет-магазин")
class Shop:
    """
    Этот класс представляет собой страницу авторизации.
    Поиск и добавление товаров в корзину.
    """
    @allure.step("Открыть сайт магазина")
    def __init__(self, driver) ->None:
        """
            Эта функция открывает страницу магазина.
            Разворачивает окно в максимальный размер.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    @allure.step("Авторизоваться")
    def authorization(self)-> None:
        """
        Эта функция находит поля авторизации.
        Вводит данные для авторизации(логин, пароль).
        Нажимает кнопку входа.
        """
        self._driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self._driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self._driver.find_element(By.ID, 'login-button').click()
        WebDriverWait(self._driver, 10)

    @allure.step("Добавить в корзину товары")
    def buy_item(self) -> None:
        """
        Находит товары на странице.
        Добавляет товары в корзину.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
