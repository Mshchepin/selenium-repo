import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#wd = webdriver.Chrome()
@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get('http://localhost/litecart/public_html/admin/login.php')

    driver.find_element(By.NAME, "username").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys('admin')
    button = driver.find_element(By.NAME, "login")
    time.sleep(3)
    button.click()
    time.sleep(3)
