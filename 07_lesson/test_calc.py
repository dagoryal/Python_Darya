import pytest
from selenium import webdriver
from CalcPage import CalcPage

def test_calc():
    driver = webdriver.Chrome()
    calc = CalcPage(driver)

    calc.delay('45')
    calc.calculator()
    res = calc.result()

    assert res == '15'

    driver.quit()
