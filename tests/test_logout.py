from conftest import *

from locators import *
class TestLogout:



    def test_account_log_out (self, mail_gen, pass_gen, wait_for_visibility):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(6)
        driver.find_element(name_field).send_keys("Иван")  # поле Имя
        driver.find_element(email_field).send_keys(mail)  # поле Email
        driver.find_element(password_field).send_keys(password)
        driver.find_element(registration_button).click()  # кнопка зарегистрироваться
        wait_for_visibility(driver, login_button)
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(email_field).send_keys(mail)  # поле Email
        driver.find_element(password_field).send_keys(password)  # поле Пароль
        driver.find_element(login_button).click()  # кнопка Войти
        wait_for_visibility(driver, profile_button)
        driver.find_element(profile_button).click()  # кнопка Личный кабинет
        wait_for_visibility(driver, logout_button)
        driver.find_element(logout_button).click() # кнопка Выход
        wait_for_visibility(driver, login_button)
        assert "Вход" in driver.find_element(login_button).text
        driver.quit()