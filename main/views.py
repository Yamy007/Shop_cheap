from django.shortcuts import render, HttpResponse

import requests
from bs4 import BeautifulSoup
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'main/home.html')



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def silpo(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        options = webdriver.ChromeOptions()
        options.add_argument("--disable")
        options.add_argument("--headless")
        driver = webdriver.Chrome("D:\Проект\chromedriver.exe", options=options)
        driver.get(f'https://shop.silpo.ua/search/all?find={product_name}')
        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'span')))
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        title = driver.find_elements(By.CLASS_NAME, "product-title")
        response_title = []
        for tit in title:
            response_title.append(tit.text)
        
        price = driver.find_elements(By.CLASS_NAME, "current-integer")
        response_price = []
        for pri in price:
            response_price.append(pri.text)
        
        mylist = zip(response_title, response_price)
        context = {
                    'mylist': mylist,
        }
        # Close the browser and return the price
        driver.quit()
        return render(request, 'main/price.html', context)
    else:
        return render(request, 'main/get_price.html')

