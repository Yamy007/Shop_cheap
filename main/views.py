from django.shortcuts import render, HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'main/home.html')




def get_price(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        url = f"https://shop.silpo.ua/search/all?find={product_name}"
        driver.get(url)
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, WebDriverWait(driver, 10).until(element_present)))
        except TimeoutException:
            return render(request, 'main/price.html', {'price': 'Ціну не вдалося знайти'})
        product_link = driver.find_element_by_class_name('.search-results-list .product-title a')
        product_link.click()

        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, WebDriverWait(driver, 10).until(element_present)))
        except TimeoutException:
            return render(request, 'main/price.html', {'price': 'Ціну не вдалося знайти'})

        price_element = driver.find_element_by_class_name('product-current')
        price = price_element.text.strip()

        driver.quit()
        return render(request, 'main/price.html', {'price': price})
    else:
        return render(request, 'main/get_price.html')


