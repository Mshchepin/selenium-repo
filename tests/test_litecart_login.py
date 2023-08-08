import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#wd = webdriver.Chrome()
#wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Nightly\\firefox.exe")
@pytest.fixture
def driver(request):
    #binary = FirefoxBinary('C:\Program Files\Firefox Nightly\firefox.exe')
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):
    driver.get('http://localhost/litecart/public_html/admin/login.php')

    driver.find_element(By.NAME, "username").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys('admin')
    button = driver.find_element(By.NAME, "login")
    button.click()




