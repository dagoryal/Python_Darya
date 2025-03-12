import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_but(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.find_element(By.NAME, 'first-name').send_keys("Иван")
    driver.find_element(By.NAME, 'last-name').send_keys("Петров")
    driver.find_element(By.NAME, 'address').send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, 'zip-code').send_keys("")
    driver.find_element(By.NAME, 'city').send_keys("Москва")
    driver.find_element(By.NAME, 'country').send_keys("Россия")
    driver.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
    driver.find_element(By.NAME, 'phone').send_keys("+7985899998787")
    driver.find_element(By.NAME, 'job-position').send_keys("QA")
    driver.find_element(By.NAME, 'company').send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 10)
    no_but = wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "button[type='submit']")))

    zip_col = driver.find_element(By.ID, 'zip-code').value_of_css_property('background-color')
    rgba = 'rgba(248, 215, 218, 1)'
    assert zip_col == rgba

    green = 'rgba(209, 231, 221, 1)'
    assert driver.find_element(By.ID, 'first-name').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'last-name').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'address').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'city').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'country').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'e-mail').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'phone').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'job-position').value_of_css_property('background-color') == green
    assert driver.find_element(By.ID, 'company').value_of_css_property('background-color') == green

    driver.quit()
