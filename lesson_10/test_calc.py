import allure
import pytest
from selenium import webdriver
from CalcPage import CalcPage

@allure.suite("Калькулятор")
@allure.title("Тестирование калькулятора")
@allure.description("Проверка корректности отображаемого результата")
@allure.feature("Нажатие кнопок. Актуальность результата")
@allure.severity("critical")
def test_calc():
    with allure.step("Перейти на страницу калькулятора"):
        driver = webdriver.Chrome()
        calc = CalcPage(driver)

    with allure.step("Ввести время ожидания"):
        calc.delay('45')

    calc.calculator()
    res = calc.result()

    with allure.step("Проверить, что в окне отобразился корректный результат через 45 секунд"):
        assert res == '15'

    driver.quit()
