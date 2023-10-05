import time

import re
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
    wait = WebDriverWait(driver, 10)
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

    FontSize_MainPageProductRegularPrice = MainPageProductRegularPrice.value_of_css_property("font-size")
    FontSize_MainPageProductCampaignPrice = MainPageProductCampaignPrice.value_of_css_property("font-size")

    FontSize_MainPageProductRegularPrice = re.findall(r'\d+\.\d+', FontSize_MainPageProductRegularPrice)
    FontSize_MainPageProductCampaignPrice = re.findall(r'\d+', FontSize_MainPageProductCampaignPrice)

    FontSize_MainPageProductRegularPrice = list(map(float, FontSize_MainPageProductRegularPrice))
    FontSize_MainPageProductCampaignPrice = list(map(int, FontSize_MainPageProductCampaignPrice))


    print("Размер шрифта обычной цены" + str(FontSize_MainPageProductRegularPrice))
    print("Размер шрифта акционной цены" + str(FontSize_MainPageProductCampaignPrice))


    #Проверка, что акционная цена больше по размерам
    print(New_Size)
    print(Old_Size)
    assert New_Size.get("height") > Old_Size.get("height")
    assert New_Size.get("width") > Old_Size.get("width")

    #Проверка по размеру шрифта
    assert FontSize_MainPageProductCampaignPrice[0] > FontSize_MainPageProductRegularPrice[0]

    #Проверка, что стандартная цена перечеркнута
    assert Decor_RegularPrice == "line-through"

    #Проверка, что цвета совпадают с ожидаемыми.
    print(MainPageProductName)
    print(Color_MainPageProductRegularPrice)
    RGB_RegularPrice = re.findall(r'\d+', Color_MainPageProductRegularPrice)
    #del RGB_RegularPrice[-1:]
    RGB_RegularPrice = list(map(int, RGB_RegularPrice))
    print(RGB_RegularPrice)
    assert RGB_RegularPrice[0] == RGB_RegularPrice[1] == RGB_RegularPrice[2]


    print(Color_MainPageProductCampaignPrice)
    RGB_CampaignPrice = re.findall(r'\d+', Color_MainPageProductCampaignPrice)
    #del RGB_CampaignPrice[-1:]
    RGB_CampaignPrice = list(map(int, RGB_CampaignPrice))
    print(RGB_CampaignPrice)
    assert RGB_CampaignPrice[0] > RGB_CampaignPrice[1] & RGB_CampaignPrice[1] == RGB_CampaignPrice[2] == 0

    print(Decor_RegularPrice)
    MainPageProduct.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#box-product .title")))
    ProductPageProductName = driver.find_element(By.CSS_SELECTOR, "#box-product .title").text

    ProductPageProductRegularPrice = driver.find_element(By.CSS_SELECTOR, ".regular-price")
    ProductPageProductCampaignPrice = driver.find_element(By.CSS_SELECTOR, ".campaign-price")
    Decor_ProductRegularPrice = ProductPageProductRegularPrice.value_of_css_property("text-decoration-line")
    Color_ProductPageProductRegularPrice = ProductPageProductRegularPrice.value_of_css_property("color")
    Color_ProductPageProductCampaignPrice = ProductPageProductCampaignPrice.value_of_css_property("color")

    FontSize_ProductPageProductRegularPrice = ProductPageProductRegularPrice.value_of_css_property("font-size")
    FontSize_ProductPageProductCampaignPrice = ProductPageProductCampaignPrice.value_of_css_property("font-size")


    FontSize_ProductPageProductRegularPrice = re.findall(r'\d+', FontSize_ProductPageProductRegularPrice)
    FontSize_ProductPageProductCampaignPrice = re.findall(r'\d+', FontSize_ProductPageProductCampaignPrice)

    FontSize_ProductPageProductRegularPrice = list(map(float, FontSize_ProductPageProductRegularPrice))
    FontSize_ProductPageProductCampaignPrice = list(map(int, FontSize_ProductPageProductCampaignPrice))

    print("Размер шрифта обычной цены на странице продукта" + str(FontSize_ProductPageProductRegularPrice))
    print("Размер шрифта акционной цены на странице продукта" + str(FontSize_ProductPageProductCampaignPrice))

    #Проверка по размеру шрифта
    assert FontSize_ProductPageProductCampaignPrice[0] > FontSize_ProductPageProductRegularPrice[0]

    #Проверка на то, что текст выделен жирным (bold = 700)
    Weight_ProductPageProductCampaignPrice = ProductPageProductCampaignPrice.value_of_css_property("font-weight")
    assert Weight_ProductPageProductCampaignPrice == "700"

    #Проверка, что цвета совпадают с ожидаемыми.

    print(Color_ProductPageProductRegularPrice)
    RGB_ProductRegularPrice = re.findall(r'\d+', Color_ProductPageProductRegularPrice)
    #del RGB_RegularPrice[-1:]
    RGB_ProductRegularPrice = list(map(int, RGB_ProductRegularPrice))
    print(RGB_ProductRegularPrice)
    assert RGB_ProductRegularPrice[0] == RGB_ProductRegularPrice[1] == RGB_ProductRegularPrice[2]

    print(Color_ProductPageProductCampaignPrice)
    RGB_ProductCampaignPrice = re.findall(r'\d+', Color_ProductPageProductCampaignPrice)
    #del RGB_CampaignPrice[-1:]
    RGB_ProductCampaignPrice = list(map(int, RGB_ProductCampaignPrice))
    print(RGB_ProductCampaignPrice)
    assert RGB_ProductCampaignPrice[0] > RGB_ProductCampaignPrice[1] & RGB_ProductCampaignPrice[1] == RGB_ProductCampaignPrice[2] == 0


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




