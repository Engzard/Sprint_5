import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestConstructor:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test_account_button_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2").click() #кнопка Конструктор
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2")))
        assert "Кабинет" in driver.find_element(By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2").text
        driver.quit()
    def test_account_button_home(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div/a/svg').click() #кнопка с логотипом сайта
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2")))
        assert "Кабинет" in driver.find_element(By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2").text
        driver.quit()
