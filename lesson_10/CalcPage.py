import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    @allure.step("Открыть страницу калькулятора")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    @allure.step("Ввести количество секунд ожидания {time} в поле задержки")
    def delay(self, time: str):
        self._driver.find_element(By.ID, 'delay').clear()
        self._driver.find_element(By.ID, 'delay').send_keys(time)

    @allure.step("Нажать кнопки калькулятора: 7, +, 8, =")
    def calculator(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step("Спустя 45 секунд получить результат 15")
    def result(self):
        WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))
        fin_res = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
        return fin_res.text
