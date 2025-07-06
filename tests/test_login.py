import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestLogin:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver
    def test_home_button_log_in (self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click() # кнопка Войти в аккаунт
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert "Вход" in driver.find_element(By.TAG_NAME, "h2").text
        driver.quit()
    def test_home_account_log_in (self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.CLASS_NAME, "AppHeader_header__link__3D_hX").click()   #кнопка Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert "Вход" in driver.find_element(By.TAG_NAME, "h2").text
        driver.quit()
    def test_registration_page_log_in (self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() # кнопка Войти
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert "Вход" in driver.find_element(By.TAG_NAME, "h2").text
        driver.quit()
    def test_password_recovery_page_log_in (self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() # кнопка Войти
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert "Вход" in driver.find_element(By.TAG_NAME, "h2").text
        driver.quit()

