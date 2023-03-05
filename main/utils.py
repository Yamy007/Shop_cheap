import requests
from bs4 import BeautifulSoup


def get_product_price(product_name):
    url = f'https://www.silpo.ua/search?text={product_name}'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')   
    try:
        result = soup.find_all('div', class_='listing-item')[0]
        name = result.find('a', class_='link').text
        price = result.find('span', class_='value').text
        return name, price
    except:
        return None