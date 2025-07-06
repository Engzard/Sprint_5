import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestConstructorPage:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver
    def test_home_button_souse (self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click() # кнопка Соусы
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '// *[ @ id = "root"] / div / main / section[1] / div[2] / ul[2] / a[1]')))

    def test_home_button_toppings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click() #кнопка Начинки
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]/img')))

    def test_home_button_bread(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '//*//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click() #кнопка Булки
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/img')))