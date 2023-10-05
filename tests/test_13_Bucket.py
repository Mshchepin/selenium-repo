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
    driver.get('http://localhost/litecart/public_html/en/')


    for i in range(1, 4):
        Product = driver.find_element(By.CSS_SELECTOR, "#box-most-popular > div > ul > li:nth-child(1)")
        Product.click()
        wait.until(EC.visibility_of_element_located((By.NAME, "add_cart_product")))

        try:
            driver.find_element(By.NAME, "options[Size]").is_displayed()
        except NoSuchElementException:
            print("The element does not exist.")
        else:
            Size = driver.find_element(By.NAME, "options[Size]")
            Size.click()
            Small = driver.find_element(By.CSS_SELECTOR, "#box-product select > option:nth-child(2)")
            Small.click()
            print("Есть Size")


        AddToCartButton = driver.find_element(By.NAME, "add_cart_product")
        AddToCartButton.click()
        time.sleep(5)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"), "1"))
        print(driver.find_element(By.CSS_SELECTOR, "#cart > a.content > span.quantity"))





