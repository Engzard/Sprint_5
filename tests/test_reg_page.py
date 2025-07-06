import pytest
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestRegistrationPage:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver
    def mail_gen(domen ='mail.ru'):
        login_length = random.randint(4, 10)
        login = ''.join(random.choice(string.ascii_lowercase) for i in range(login_length))
        return f"{login}@{domen}"
    def pass_gen(lenght):
        password = ''.join(str(random.randint(0, 9)) for i in range(length))
        return password

    def test_registration_passward_6symbols_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(6)
        driver.find_element(By.NAME, "name").send_keys("Иван") # поле Имя
        driver.find_element(By.NAME, "email").send_keys(mail) # поле Email
        driver.find_element(By.NAME, "password").send_keys(password) # поле Пароль
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click() #кнопка зарегистрироваться
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert "Вход" in driver.find_element(By.TAG_NAME, "h2").text
        driver.quit()

    def test_registration_passward_7symbols_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(7)
        driver.find_element(By.NAME, "name").send_keys("Иван")  # поле Имя
        driver.find_element(By.NAME, "email").send_keys(mail) # поле Email
        driver.find_element(By.NAME, "password").send_keys(password)    # поле Пароль
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()   #кнопка зарегистрироваться
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert "Вход" in driver.find_element(By.TAG_NAME, "h2").text
        driver.quit()
    def test_registration_passward_11symbols_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(11)
        driver.find_element(By.NAME, "name").send_keys("Иван")  # поле Имя
        driver.find_element(By.NAME, "email").send_keys(mail)   # поле Email
        driver.find_element(By.NAME, "password").send_keys(password)    # поле Пароль
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()   #кнопка зарегистрироваться
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert "Вход" in driver.find_element(By.TAG_NAME, "h2").text
        driver.quit()

    def test_registration_passward_5symbols_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(15)
        driver.find_element(By.NAME, "name").send_keys("Иван")  # поле Имя
        driver.find_element(By.NAME, "email").send_keys(mail)   # поле Email
        driver.find_element(By.NAME, "password").send_keys(password)    # поле Пароль
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()    #кнопка зарегистрироваться
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error text_type_main-default")))

