from conftest import *
from locators import *

class TestConstructor:

    def test_account_button_constructor(self, driver, wait_for_visibility):
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(constructor_button).click() #кнопка Конструктор
        wait_for_visibility(driver,profile_button)
        assert "Кабинет" in driver.find_element(profile_button).text
        driver.quit()
    def test_account_button_home(self, driver, wait_for_visibility):
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(logo).click() #кнопка с логотипом сайта
        wait_for_visibility(driver,profile_button)
        assert "Кабинет" in driver.find_element(profile_button).text
        driver.quit()
