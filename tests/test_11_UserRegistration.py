import string
import time

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
@pytest.fixture
def driver(request):

    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://localhost/litecart/public_html/en/create_account')
    FirstName = driver.find_element(By.NAME, "firstname")
    LastName = driver.find_element(By.NAME, "lastname")
    Address = driver.find_element(By.NAME, "address1")
    Postcode = driver.find_element(By.NAME, "postcode")
    City = driver.find_element(By.NAME, "city")
    Random = random.randint(10000, 99999)

    FirstName.send_keys('Ivan')
    LastName.send_keys('Ivanov')
    Address.send_keys("Pushkina 5")
    Postcode.send_keys(Random)
    City.send_keys("Sochy")

    Country = driver.find_element(By.CLASS_NAME, "select2-selection__arrow")
    Country.click()
    CountrySearch = driver.find_element(By.CLASS_NAME, "select2-search__field")
    CountrySearch.send_keys("United States" + Keys.ENTER)

    State = driver.find_element(By.CSS_SELECTOR, "#create-account [name='zone_code'] > [value='CO']")
    State.click()
    print(CountrySearch)
    print(State)
    Email = driver.find_element(By.NAME, "email")
    CurrentEmail = (random.choice(string.ascii_letters) + "test" + str(Random) + "@test.ru")
    Email.send_keys(CurrentEmail)
    Phone = driver.find_element(By.NAME, "phone")
    Phone.send_keys("88005553535")
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("qwerty")
    ConfirmPassword = driver.find_element(By.NAME, "confirmed_password")
    ConfirmPassword.send_keys("qwerty")


    CreateButton = driver.find_element(By.NAME, "create_account")
    CreateButton.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#box-account > div > ul > li:nth-child(4) > a")))
    #logout

    LogoutButton = driver.find_element(By.CSS_SELECTOR, "#box-account > div > ul > li:nth-child(4) > a")
    LogoutButton.click()
    wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    #Login

    LoginEmail = driver.find_element(By.NAME, "email")
    LoginEmail.send_keys(CurrentEmail)
    LoginPassword = driver.find_element(By.NAME, "password")
    LoginPassword.send_keys("qwerty")
    LoginButton = driver.find_element(By.NAME, "login")
    LoginButton.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#box-account > div > ul > li:nth-child(4) > a")))

    #Logout2
    LogoutButton = driver.find_element(By.CSS_SELECTOR, "#box-account > div > ul > li:nth-child(4) > a")
    LogoutButton.click()
