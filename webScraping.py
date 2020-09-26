from os import name
from re import sub
import requests as req
from bs4 import BeautifulSoup
import re
#import os 
main = req.get("https://www.lioncomputer.com/computer/computer-components/processor.html?product_list_limit=92")
main = BeautifulSoup(main.text,'html.parser')
names = main.find_all('a',attrs={'class':'product-item-link'})
count = 0

for i in names[:92]:
    name = re.sub(r'[\n,\t]','',i.text.strip())
    
    link = req.get(i.get('href'))
    link = BeautifulSoup(link.text,'html.parser')
    c1  = link.find_all('th',attrs={'class':'col label'})
    c2  = link.find_all('td',attrs={'class':'col data'})
    cc1 = []
    cc2 = []
    for label in c1:
        cc1.append(label.text) 
    for data in c2:
        cc2 .append(data.text)
    xx= ''
    for l in range(0,len(cc1)):
        file = open(f'./cpu/{name}.text','w')
        
        w = f'{cc1[l]}\t{cc2[l]}\n'
        xx =xx+w
    file.write(xx)
    file.close()
    
    count +=1
    print(count+name)
print('Be Fun :)')