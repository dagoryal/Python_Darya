import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

def test_but():
    fn = (driver.find_element(By.NAME, 'first-name')
      .send_keys("Иван"))
    ln = (driver.find_element(By.NAME, 'last-name')
      .send_keys("Петров"))
    adr = (driver.find_element(By.NAME, 'address')
       .send_keys("Ленина, 55-3"))
    zip_code = (driver.find_element(By.NAME, 'zip-code')
            .send_keys(""))
    city = (driver.find_element(By.NAME, 'city')
        .send_keys("Москва"))
    country = (driver.find_element(By.NAME, 'country')
           .send_keys("Россия"))
    mail = (driver.find_element(By.NAME, 'e-mail')
        .send_keys("test@skypro.com"))
    phone = (driver.find_element(By.NAME, 'phone')
         .send_keys("+7985899998787"))
    job = (driver.find_element(By.NAME, 'job-position')
       .send_keys("QA"))
    comp = (driver.find_element(By.NAME, 'company')
        .send_keys("SkyPro"))

    but = (driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
       .click())

    wait = WebDriverWait(driver, 10)
    no_but = wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "button[type='submit']")))

    zip_col = driver.find_element(By.ID, 'zip-code').value_of_css_property('background-color')
    rgba = 'rgba(248, 215, 218, 1)'
    assert zip_col == rgba

    green = 'rgba(209, 231, 221, 1)'
    fir = driver.find_element(By.ID, 'first-name').value_of_css_property('background-color')
    last_n = driver.find_element(By.ID, 'last-name').value_of_css_property('background-color')
    var = fir == last_n 
    adrs = driver.find_element(By.ID, 'address').value_of_css_property('background-color')
    var = last_n == adrs
    cit = driver.find_element(By.ID, 'city').value_of_css_property('background-color')
    var = adrs == cit
    con = driver.find_element(By.ID, 'country').value_of_css_property('background-color')
    var = cit == con
    e_mail = driver.find_element(By.ID, 'e-mail').value_of_css_property('background-color')
    var = con == e_mail
    phone_num = driver.find_element(By.ID, 'phone').value_of_css_property('background-color')
    var = e_mail == phone_num
    jbb = driver.find_element(By.ID, 'job-position').value_of_css_property('background-color')
    var = phone_num == jbb
    cmp = driver.find_element(By.ID, 'company').value_of_css_property('background-color')
    var = jbb == cmp

    assert  green == fir
