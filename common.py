#conding=utf8  
import os 
from bs4 import BeautifulSoup
import re





def getAllHtml(mypath):
    '''
    1.查找文件目录下的所有html 
    input ：文件路径
    output：所有html的list
    '''
    g = os.walk(mypath)  
    res = []
    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            if file_name.endswith('.html'):
                res.append(os.path.join(path, file_name))
    return res



'''
2.找出html的title
input ：文件路径
output：html的title的内容
'''

def hasText(htmlPath,text):
    '''
    3.html查找所有是否包含关键字
    input ：文件路径，关键字
    output：T/F
    '''
    with open(htmlPath, 'r', encoding='utf-8') as f:
        Soup = BeautifulSoup(f.read(), 'html.parser')
    te = re.compile(text)
    finds = Soup.find_all(text=te)

    if finds :
        print(htmlPath)
        for i in finds:
            print(i)
        print('-'*50)
        return  True
    return False

def replace_title(htmlPath,oldName,newName):
    '''
    4.替换html中的标题关键字
    input ：文件路径，查找的关键字，替换的关键字
    output：T/F
    '''
    with open(htmlPath, 'r', encoding='utf-8') as f:
        Soup = BeautifulSoup(f.read(), 'html.parser')
        aa = Soup.find('title')
        te = re.compile(oldName)

    if aa :
        if aa.find(text=te) :
            tempOld = aa.find(text=te)
            aa.find(text=te).replace_with(newName)
            with open(htmlPath, 'w',encoding="utf-8") as fp:
                fp.write(Soup.prettify())
            print(htmlPath)
            print('修改成功   ',tempOld.strip(),'->',newName.strip())
            return True
        else:
            print(htmlPath )
            print('未修改   当前title为: '+aa.string.strip())
            return False
    else:
        # print(htmlPath)
        # print('未修改   没有找到title')
        return False

