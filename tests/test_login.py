
from locators import *

class TestLogin:

    def test_home_button_log_in (self, driver, wait_for_visibility):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(log_in_account_button).click() # кнопка Войти в аккаунт
        wait_for_visibility(driver,login_button)
        assert "Вход" in driver.find_element(login_button_after_reg).text
    def test_home_account_log_in (self, driver, wait_for_visibility):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(profile_button).click() #кнопка Личный кабинет
        wait_for_visibility(driver,login_button)
        assert "Вход" in driver.find_element(login_button_after_reg).text
    def test_registration_page_log_in (self, driver, wait_for_visibility):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(login_link).click() # кнопка Войти
        wait_for_visibility(driver,login_button)
        assert "Вход" in driver.find_element(login_button_after_reg).text
    def test_password_recovery_page_log_in (self, driver, wait_for_visibility):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(login_link).click() # кнопка Войти
        wait_for_visibility(driver,login_button)
        assert "Вход" in driver.find_element(login_button_after_reg).text
