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
    wd.implicitly_wait(3)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):

    driver.get('http://localhost/litecart/public_html/en/')
    time.sleep(1)
    products = driver.find_elements(By.CSS_SELECTOR, ".product")
    for i in range (0, len(products)):
        sticker = products[i].find_elements(By.CSS_SELECTOR, ".sticker")
        assert len(sticker) == 1


        #for j in range(0, len(sticker)):
            #with open('output.txt', 'a') as f:
                #f.write("\nnumber of products are " + str(len(products)))
                #f.write(sticker[j].text + str(len(sticker)))










