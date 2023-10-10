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
    driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
    driver.find_element(By.NAME, "username").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys('admin')
    button = driver.find_element(By.NAME, "login")
    button.click()

    AddNewCountryButton = driver.find_element(By.CSS_SELECTOR, "#content > div > a")
    AddNewCountryButton.click()
    wait.until(EC.element_to_be_clickable((By.NAME, "save")))
    External_Links = driver.find_elements(By.CSS_SELECTOR, ".fa.fa-external-link")
    time.sleep(3)
    for i in range(0, len(External_Links)):
        Main_window = driver.current_window_handle
        Old_window = driver.window_handles
        External_Links[i].click()
        wait.until(EC.new_window_is_opened(Old_window))
        New_window = driver.window_handles
        New_window = list(set(New_window).difference(Old_window))
        print(New_window)
        driver.switch_to.window(New_window[0])
        driver.close()
        driver.switch_to.window(Main_window)


