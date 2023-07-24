import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#wd = webdriver.Chrome()
@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get('https://www.google.ru/?hl=ru')
    driver.find_element(By.NAME, "q").send_keys('webdriver')
    button = driver.find_element(By.NAME, "btnK")
    time.sleep(3)
    button.click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))


if __name__ == '__main__':
    print('PyCharm1')

#     wd.get("https://www.google.com/")
#     q = wd.find_element(By.NAME, "q")
#     q.send_keys("webdriver")
#     time.sleep(3)
#     b = wd.find_element(By.NAME, "btnK")
#     b.is_displayed()
#     b.click()
#     #time.sleep(5)
#     WebDriverWait(wd, 10).until(EC.title_is("webdriver - Поиск в Google"))
