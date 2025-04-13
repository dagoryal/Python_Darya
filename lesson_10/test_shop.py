import allure
import pytest
from selenium import webdriver
from ShopPage import Shop
from ShopCartPage import CartPage
from ShopInfoPage import InfoPage

@allure.suite("Интернет-магазин")
@allure.title("Проверки функциональности интернет-магазина")
@allure.description("Автоматизация покупки")
@allure.feature("Авторизация. Корзина. Форма")
@allure.severity("critical")
def test_shop():
    driver = webdriver.Chrome()
    main_shop = Shop(driver)

    main_shop.authorization()
    main_shop.buy_item()

    cart_page = CartPage(driver)
    cart_page.get()

    info_page = InfoPage(driver)
    info_page.get()
    info_page.info()
    overview = info_page.total()

    driver.quit()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert overview == 'Total: $58.29'
