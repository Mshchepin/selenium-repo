import string
import time

import os
import re
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.keys import Keys
from datetime import datetime
@pytest.fixture
def driver(request):

    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog')
    driver.find_element(By.NAME, "username").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys('admin')
    button = driver.find_element(By.NAME, "login")
    button.click()



    #Открыть папки
    driver.find_element(By.CSS_SELECTOR, "#content > form > table > tbody > tr:nth-child(3) > td:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#content > form > table > tbody > tr:nth-child(4) > td:nth-child(3) > a").click()
    Elements = driver.find_elements(By.CSS_SELECTOR, "#content > form > table > tbody > tr > td:nth-child(3) > a")
    for element in range(0, len(Elements)):
        Elements = driver.find_elements(By.CSS_SELECTOR, "#content > form > table > tbody > tr > td:nth-child(3) > a")
        Elements[element].click()
        for log in driver.get_log("browser"):
            print(log)
        driver.find_element(By.NAME, "cancel").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div:nth-child(2) > a:nth-child(2)")))


#content > form > table > tbody > tr:nth-child(4) > td:nth-child(3) > a
