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

def metod(driver):
    driver.get('http://localhost/litecart/public_html/admin/login.php')

    driver.find_element(By.NAME, "username").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys('admin')
    button = driver.find_element(By.NAME, "login")
    button.click()
    sidebar = driver.find_element(By.ID, "box-apps-menu")
    elements = sidebar.find_elements(By.ID, "app")
    for item in range (0, len(elements)):
        item.click()



if __name__ == '__main__':
    #print('PyCharm1')
    metod()
#     wd.get("https://www.google.com/")
#     q = wd.find_element(By.NAME, "q")
#     q.send_keys("webdriver")
#     time.sleep(3)
#     b = wd.find_element(By.NAME, "btnK")
#     b.is_displayed()
#     b.click()
#     #time.sleep(5)
#     WebDriverWait(wd, 10).until(EC.title_is("webdriver - Поиск в Google"))
