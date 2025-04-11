import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.suite("Интернет-магазин")
class InfoPage:
    """
    Этот класс содержит в себе методы заполнения формы.
    Проверка итоговой стоимости.
    """
    def __init__(self, driver):
        self._driver = driver

    def get(self) -> None:
        """
        Функция страницы оформления заказа.
        """
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')

    @allure.step("Заполнить форму данными")
    def info(self) -> None:
        """
        Эта функция заполняет форму данными.
        Нажимает кнопку "continue".
        """
        self._driver.find_element(By.ID, 'first-name').send_keys('Darya')
        self._driver.find_element(By.ID, 'last-name').send_keys('Gorchakova')
        self._driver.find_element(By.ID, 'postal-code').send_keys('123456')
        self._driver.find_element(By.ID, 'continue').click()

    @allure.step("Прочитать итоговую стоимость")
    def total(self) -> str:
        """
        Эта функция находит итоговую стоимость.
        :return: Результат в виде текста.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label')))
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label')
        return total.text
