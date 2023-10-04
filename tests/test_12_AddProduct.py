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
    time.sleep(5)
    AddProductButton = driver.find_element(By.CSS_SELECTOR, "#content .button:last-child")
    AddProductButton.click()
    CurrentName = "Test Product" + str(datetime.now())

    Name = driver.find_element(By.NAME, "name[en]")
    Name.send_keys(CurrentName)
    Code = driver.find_element(By.NAME, "code")
    Code.send_keys("T001")
    Gender = driver.find_element(By.CSS_SELECTOR, "#tab-general > table > tbody [name = 'product_groups[]'][value = '1-1']")
    Gender.click()

    Quantity = driver.find_element(By.NAME, "quantity")
    Quantity.clear()
    Quantity.send_keys("10")
    Image = driver.find_element(By.NAME, "new_images[]")
    Image.send_keys(os.path.abspath("logo.jpg"))


    Information = driver.find_element(By.CSS_SELECTOR, "#content > form > div > ul > li:nth-child(2) > a")
    Information.click()
    time.sleep(5)
    Manufacturer = driver.find_element(By.NAME, "manufacturer_id")
    Manufacturer.click()
    ACMECorp = driver.find_element(By.CSS_SELECTOR, "#tab-information > table > tbody [value = '1']")
    ACMECorp.click()

    Keywords = driver.find_element(By.NAME, "keywords")
    Keywords.send_keys("Test")
    Short_Descriprion = driver.find_element(By.NAME, "short_description[en]")
    Short_Descriprion.send_keys("Test Short Description")
    Descriprion = driver.find_element(By.CSS_SELECTOR, "#tab-information > table > tbody > tr:nth-child(5) > td > span > div > div.trumbowyg-editor")
    Descriprion.send_keys("Test Description")

    Prices = driver.find_element(By.CSS_SELECTOR, "#content > form > div > ul > li:nth-child(4) > a")
    Prices.click()
    time.sleep(5)

    PurchasePrice = driver.find_element(By.NAME, "purchase_price")
    PurchasePrice.clear()
    PurchasePrice.send_keys("10")

    CurrencyCode = driver.find_element(By.NAME, "purchase_price_currency_code")
    CurrencyCode.click()
    CurrencyUSD = driver.find_element(By.CSS_SELECTOR, "#tab-prices [value = 'USD']")
    CurrencyUSD.click()
    PriceUSD = driver.find_element(By.NAME, "prices[USD]")
    PriceUSD.send_keys("10")
    PriceEUR = driver.find_element(By.NAME, "prices[EUR]")
    PriceEUR.send_keys("10")


    SaveButton = driver.find_element(By.NAME, "save")
    SaveButton.click()
    time.sleep(5)
    AddedProduct = driver.find_element(By.XPATH, "//a[text()='" + CurrentName + "']")
    AddedProduct.click()
    time.sleep(5)
    #Удалить добавленный продукт

