import pytest
from selenium import webdriver
from FormMainPage import MainPage


def test_form():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)

    main_page.set_form_data()
    main_page.find()

    main_page.time_page()

    main_page.zip_color()
    main_page.green_color()

    driver.quit()
