from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()

    def set_form_data(self):
        self._driver.find_element(By.NAME, 'first-name').send_keys("Иван")
        self._driver.find_element(By.NAME, 'last-name').send_keys("Петров")
        self._driver.find_element(By.NAME, 'address').send_keys("Ленина, 55-3")
        self._driver.find_element(By.NAME, 'zip-code').send_keys("")
        self._driver.find_element(By.NAME, 'city').send_keys("Москва")
        self._driver.find_element(By.NAME, 'country').send_keys("Россия")
        self._driver.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
        self._driver.find_element(By.NAME, 'phone').send_keys("+7985899998787")
        self._driver.find_element(By.NAME, 'job-position').send_keys("QA")
        self._driver.find_element(By.NAME, 'company').send_keys("SkyPro")

    def find(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def time_page(self):
        WebDriverWait(self._driver, 15).until(EC.invisibility_of_element((By.CSS_SELECTOR, "button[type='submit']")))

    def zip_color(self):
        zip_col = self._driver.find_element(By.ID, 'zip-code').value_of_css_property('background-color')
        rgba = 'rgba(248, 215, 218, 1)'
        assert zip_col == rgba

    def green_color(self):
        green = 'rgba(209, 231, 221, 1)'
        assert self._driver.find_element(By.ID, 'first-name').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'last-name').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'address').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'city').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'country').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'e-mail').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'phone').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'job-position').value_of_css_property('background-color') == green
        assert self._driver.find_element(By.ID, 'company').value_of_css_property('background-color') == green
