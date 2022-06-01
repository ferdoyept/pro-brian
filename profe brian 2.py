
from bs4 import BeautifulSoup 
import requests


result = requests.get('https://tienda.att.com.mx/outlet-en-att/huawei-watch-gt2-e-hua-wat-gt-2e-1')
content = result.text
soup = BeautifulSoup(content, 'lxml')
item = soup.find('li' , class_= 'item product product-item outlet-en-att')
product = item.find('a', class_= 'product-item-link').get_text()
price =item.find('span', class_= 'price').get_text()
print(product)