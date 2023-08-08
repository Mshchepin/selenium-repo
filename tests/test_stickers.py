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
    stickers = driver.find_elements(By.CSS_SELECTOR, ".image-wrapper")
    for i in range (0, len(stickers)):
        stickersonsale = stickers[i].find_elements(By.CSS_SELECTOR, ".sticker.sale")
        stickersnew = stickers[i].find_elements(By.CSS_SELECTOR, ".sticker.new")

        EC.visibility_of(stickers)
        assert len(stickersonsale) + len(stickersnew) == 1

        #with open('output.txt', 'a') as f:
            #f.write("\nnumber of stickers are " + str(len(stickers)))
            #f.write(stickers[i].text)










