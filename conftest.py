import pytest
from selenium import webdriver
import string
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver
@pytest.fixture
def mail_gen(domain ='mail.ru'):
    login_length = random.randint(4, 10)
    login = ''.join(random.choice(string.ascii_lowercase) for i in range(login_length))
    return f"{login}@{domain}"
@pytest.fixture
def pass_gen():
    def _gen (length):
        return ''.join(str(random.randint(0, 9)) for i in range(length))
    return _gen
@pytest.fixture
def wait_for_visibility(driver):
    def _wait(locator, time = 10):
        return WebDriverWait(driver, time).until(expected_conditions.visibility_of_element_located(locator))
    return _wait
@pytest.fixture
def wait_class_change(driver):
    def _wait(locator, time = 10):
        return WebDriverWait(driver, time).until(expected_conditions.text_to_be_present_in_element_attribute(locator, "class", "tab_tab_type_current__2BEPc") )
    return _wait
