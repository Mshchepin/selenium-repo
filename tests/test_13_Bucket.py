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
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"), str(i)))
        print(driver.find_element(By.CSS_SELECTOR, "#cart > a.content > span.quantity"))
        HomeButton = driver.find_element(By.CSS_SELECTOR, "#site-menu > ul > li.general-0 > a > i")
        HomeButton.click()
    CheckoutButton = driver.find_element(By.CSS_SELECTOR, "#cart > a.link")
    CheckoutButton.click()
    wait.until(EC.element_to_be_clickable((By.NAME, "remove_cart_item")))
    time.sleep(2)
    while len(driver.find_elements(By.CSS_SELECTOR, "#order_confirmation-wrapper > table > tbody > tr:nth-child(2)")) > 0:
        wait.until(EC.element_to_be_clickable((By.NAME, "remove_cart_item")))
        RemoveButton = driver.find_element(By.NAME, "remove_cart_item")
        RemoveButton.click()
        print("Deleted")
        time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout-cart-wrapper > p:nth-child(1) > em")))
    #assert len(driver.find_elements(By.CSS_SELECTOR, "#order_confirmation-wrapper > table > tbody > tr:nth-child(2)")) == 0




