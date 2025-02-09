from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_button1(browser):
    browser.get('https://infodialog.ru/products')
    pp = browser.find_element(By.CLASS_NAME, 'red-title')
    assert pp.text == '''Продукты компании\nInfodialog'''