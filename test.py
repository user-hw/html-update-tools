#conding=utf8  
from msilib import type_binary
import os
from bs4 import BeautifulSoup
import re


mypath = 'E:/suanpan-desktop/components/rpa/assets/login.html'


with open(mypath, 'r', encoding='utf-8') as f:
    Soup = BeautifulSoup(f.read(), 'html.parser')
    print(Soup)
    aa = Soup.find('title')
    
    
    te = re.compile('雪浪')

if aa.find(text=te):
    
    aa.find(text=te).replace_with('新的标题')
    with open(mypath, 'w',encoding="utf-8") as fp:

        fp.write(Soup.prettify())
else:
    print('aaaa')


    
