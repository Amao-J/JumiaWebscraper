from re import search
from bs4 import BeautifulSoup
import requests
from csv import writer


search = input(
    'what do you want to search for :'
)


url = "https://www.jumia.com.ng/catalog/?q=%s"%(search)
page = requests.get(url)


data = BeautifulSoup(page.content, 'html.parser')
lists = data.find_all('div',class_='info')
with open('jumia.csv', 'w', encoding='utf-8',newline='') as f:
        
    thewriter = writer(f)
    header=['Name','Price']
    thewriter.writerow(header)
    for list in lists:
        name = list.find('h3', class_= 'name').text
        price = list.find('div',class_='prc').text
        info=[name,price]
        thewriter.writerow(info)
