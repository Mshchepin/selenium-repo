import time

import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
@pytest.fixture
def driver(request):

    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):

    driver.get('http://localhost/litecart/public_html/en/')
    MainPageProduct = driver.find_element(By.CSS_SELECTOR, "#box-campaigns .product")
    MainPageProductName = driver.find_element(By.CSS_SELECTOR, "#box-campaigns .product:first-child [class=name]").text
    MainPageProductRegularPrice = driver.find_element(By.CSS_SELECTOR, "#box-campaigns .product:first-child s")
    MainPageProductCampaignPrice = driver.find_element(By.CSS_SELECTOR, "#box-campaigns .product:first-child strong")
    Old_Price = MainPageProductRegularPrice.text
    New_Price = MainPageProductCampaignPrice.text
    Old_Size = MainPageProductRegularPrice.size
    New_Size = MainPageProductCampaignPrice.size
    Decor_RegularPrice = MainPageProductRegularPrice.value_of_css_property("text-decoration-line")
    Color_MainPageProductRegularPrice = MainPageProductRegularPrice.value_of_css_property("color")
    Color_MainPageProductCampaignPrice = MainPageProductCampaignPrice.value_of_css_property("color")

    #Проверка, что цвета совпадают с ожидаемыми. Для этого беру эталонный цвет и сравниваю с полученным в hex
    hexGray = Color.from_string(Color_MainPageProductRegularPrice).hex
    hexRed = Color.from_string(Color_MainPageProductCampaignPrice).hex
    assert hexGray == "#777777"
    assert hexRed == "#cc0000"

    #Проверка, что акционная цена больше по размерам
    print(New_Size)
    print(Old_Size)
    assert New_Size.get("height") > Old_Size.get("height")
    assert New_Size.get("width") > Old_Size.get("width")
    #Проверка, что стандартная цена перечеркнута
    assert Decor_RegularPrice == "line-through"


    print(MainPageProductName)
    print(Color_MainPageProductRegularPrice)
    print(Color_MainPageProductCampaignPrice)
    print(Decor_RegularPrice)
    MainPageProduct.click()
    time.sleep(3)



    ProductPageProductName = driver.find_element(By.CSS_SELECTOR, "#box-product .title").text
    ProductPageProductRegularPrice = driver.find_element(By.CSS_SELECTOR, ".regular-price")
    ProductPageProductCampaignPrice = driver.find_element(By.CSS_SELECTOR, ".campaign-price")
    Decor_ProductRegularPrice = ProductPageProductRegularPrice.value_of_css_property("text-decoration-line")
    Color_ProductPageProductRegularPrice = ProductPageProductRegularPrice.value_of_css_property("color")
    Color_ProductPageProductCampaignPrice = ProductPageProductCampaignPrice.value_of_css_property("color")

    #Проверка на то, что текст выделен жирным (bold = 700)
    Weight_ProductPageProductCampaignPrice = ProductPageProductCampaignPrice.value_of_css_property("font-weight")
    assert Weight_ProductPageProductCampaignPrice == "700"

    #Проверка, что цвета совпадают с ожидаемыми. Для этого беру эталонный цвет и сравниваю с полученным в hex
    ProducthexGray = Color.from_string(Color_ProductPageProductRegularPrice).hex
    ProducthexRed = Color.from_string(Color_ProductPageProductCampaignPrice).hex
    assert ProducthexGray == "#666666"
    assert ProducthexRed == "#cc0000"

    Old_Price1 = ProductPageProductRegularPrice.text
    New_Price1 = ProductPageProductCampaignPrice.text
    Old_Size1 = ProductPageProductRegularPrice.size
    New_Size1 = ProductPageProductCampaignPrice.size
    assert New_Size1.get("height") > Old_Size1.get("height")
    assert New_Size1.get("width") > Old_Size1.get("width")
    assert Decor_ProductRegularPrice == "line-through"

    assert MainPageProductName == ProductPageProductName
    assert Old_Price == Old_Price1
    assert New_Price == New_Price1




