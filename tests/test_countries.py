import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):

    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):

    driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
    driver.find_element(By.NAME, "username").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys('admin')
    button = driver.find_element(By.NAME, "login")
    button.click()
    country_list = []
    countriesCount = driver.find_elements(By.CSS_SELECTOR, ".row")
    for i in range (0, len(countriesCount)):
        countriesCount = driver.find_elements(By.CSS_SELECTOR, ".row")
        CountryName = countriesCount[i].find_element(By.CSS_SELECTOR, ".row td:nth-child(5)").text
        country_list.append(CountryName)
        Zones = countriesCount[i].find_element(By.CSS_SELECTOR, ".row td:nth-child(6)").text
        if int(Zones) > 0:
            zones_list = []
            countriesCount[i].find_element(By.CSS_SELECTOR, ".row td:nth-child(7)").click()
            time.sleep(3)
            zonesCount = driver.find_elements(By.CSS_SELECTOR, ".dataTable tr")
            for j in range (1, len(zonesCount)-1):
                ZoneName = zonesCount[j].find_element(By.CSS_SELECTOR, ".dataTable tr td:nth-child(3)").text
                zones_list.append(ZoneName)
            assert zones_list == sorted(zones_list)
            print(zones_list)
            driver.find_element(By.CSS_SELECTOR, "button + [name='cancel']").click()
    print(country_list)
    assert country_list == sorted(country_list)











