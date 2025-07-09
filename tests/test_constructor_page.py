from conftest import *

from locators import *
class TestConstructorPage:

    def test_home_button_souse (self, driver, wait_class_change):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(souses_button).click() # кнопка Соусы
        wait_class_change(driver, souses_button)
        assert ('noselect' in driver.find_element(bread_button).get_attribute("class")) and ('noselect' in driver.find_element(toppings_button).get_attribute("class"))

    def test_home_button_toppings(self, driver, wait_class_change):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(toppings_button).click() # кнопка Соусы
        wait_class_change(driver, toppings_button)
        assert ('noselect' in driver.find_element(bread_button).get_attribute("class")) and ('noselect' in driver.find_element(souses_button).get_attribute("class"))

    def test_home_button_bread(self, driver, wait_class_change):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(bread_button).click() # кнопка Соусы
        wait_class_change(driver, bread_button)
        assert ('noselect' in driver.find_element(souses_button).get_attribute("class")) and ('noselect' in driver.find_element(toppings_button).get_attribute("class"))
