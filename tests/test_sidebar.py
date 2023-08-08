import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException

import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#wd = webdriver.Chrome()
#wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Nightly\\firefox.exe")
@pytest.fixture
def driver(request):
    #binary = FirefoxBinary('C:\Program Files\Firefox Nightly\firefox.exe')
    wd = webdriver.Chrome()
    wd.implicitly_wait(3)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):

    driver.get('http://localhost/litecart/public_html/admin/login.php')

    driver.find_element(By.NAME, "username").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys('admin')
    button = driver.find_element(By.NAME, "login")
    button.click()
    time.sleep(3)
    sidebar = driver.find_elements(By.XPATH, ".//*[@id='app-']")
    for countI in range (0, len(sidebar)):
        sidebar = driver.find_elements(By.XPATH, ".//*[@id='app-']")
        sidebar[countI].click()
        submenu = driver.find_elements(By.XPATH, "//*[@id='app-']/ul/li")
        for countJ in range(0, len(submenu)):
            submenu = driver.find_elements(By.XPATH, "//*[@id='app-']/ul/li")
            submenu[countJ].click()
            h1label = driver.find_element(By.XPATH, "//*[@id='content']/h1")
            EC.visibility_of_element_located(h1label)







