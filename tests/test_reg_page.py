from conftest import *

from locators import *

class TestRegistrationPage:
    def test_registration_passward_6symbols_success(self, driver, mail_gen, pass_gen, wait_for_visibility):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(6)
        driver.find_element(name_field).send_keys("Иван") # поле Имя
        driver.find_element(email_field).send_keys(mail) # поле Email
        driver.find_element(password_field).send_keys(password) # поле Пароль
        driver.find_element(registration_button).click() #кнопка зарегистрироваться
        wait_for_visibility(driver,login_button)
        assert "Вход" in driver.find_element(login_button_after_reg).text
        driver.quit()

    def test_registration_passward_7symbols_success(self, driver, mail_gen, pass_gen):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(7)
        driver.find_element(name_field).send_keys("Иван")  # поле Имя
        driver.find_element(email_field).send_keys(mail) # поле Email
        driver.find_element(password_field).send_keys(password)    # поле Пароль
        driver.find_element(registration_button).click()   #кнопка зарегистрироваться
        wait_for_visibility(driver,login_button)
        assert "Вход" in driver.find_element(login_button_after_reg).text
        driver.quit()
    def test_registration_passward_11symbols_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(11)
        driver.find_element(name_field).send_keys("Иван")  # поле Имя
        driver.find_element(email_field).send_keys(mail)   # поле Email
        driver.find_element(password_field).send_keys(password)    # поле Пароль
        driver.find_element(registration_button).click()   #кнопка зарегистрироваться
        wait_for_visibility(driver, login_button)
        assert "Вход" in driver.find_element(login_button_after_reg).text
        driver.quit()

    def test_registration_passward_5symbols_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        mail = mail_gen()
        password = pass_gen(15)
        driver.find_element(name_field).send_keys("Иван")  # поле Имя
        driver.find_element(email_field).send_keys(mail)   # поле Email
        driver.find_element(password_field).send_keys(password)    # поле Пароль
        driver.find_element(registration_button).click()    #кнопка зарегистрироваться
        wait_for_visibility(driver, password_error_text)
        assert "Некорректный пароль" in driver.find_element(password_error_text).text
        driver.quit()
