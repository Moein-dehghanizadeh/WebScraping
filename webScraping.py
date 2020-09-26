from os import name
from re import sub
import requests as req
from bs4 import BeautifulSoup
import re
from statistics import mean
def get_site(link):
    site = req.get(link)
    site = BeautifulSoup(site.text,'html.parser')
    return site
def re_sub(string):
    string = re.sub(r'[\n,\t]','',string.strip())
    return string
main = get_site("https://www.lioncomputer.com/computer/computer-components/processor.html?product_list_limit=92")
names = main.find_all('a',attrs={'class':'product-item-link'})
prices = main.find_all('span',attrs={'class':'price'})
count = 0
for i in range(0,92):
    name = names[i].text
    price = int(re.sub(r'["تومان",","]','',prices[i].text.strip()))/1000000
    print(name,price)

print()
print('-----------------------')
print()
print('Be Fun :-)')