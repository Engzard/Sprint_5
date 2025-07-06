from selenium import webdriver
import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestAccount:
    def mail_gen(domen ='mail.ru'):
        login_length = random.randint(4, 10)
        login = ''.join(random.choice(string.ascii_lowercase) for i in range(login_length))
        return f"{login}@{domen}"
    def pass_gen(lenght):
        password = ''.join(str(random.randint(0, 9)) for i in range(length))
        return password

    def test_home_account (self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(6)
        driver.find_element(By.NAME, "name").send_keys("Иван") # поле Имя
        driver.find_element(By.NAME, "email").send_keys(mail) # поле Email
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click() #кнопка зарегистрироваться
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.NAME, "email").send_keys(mail) # поле Email
        driver.find_element(By.NAME, "password").send_keys(password) # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click() #кнопка Войти
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2")))
        driver.find_element(By.CLASS_NAME, "AppHeader_header__linkText__3q_va ml-2").click()  #кнопка Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/account/profile']")))
        assert "Профиль" in driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a').text
        driver.quit()