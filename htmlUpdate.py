import click
from service import find_text_in_html,replace_all_title

with open('MyPath.txt','r',encoding='utf-8') as f:
    MYPATH = f.read()

@click.group()
def cli():
    pass

@cli.command()
@click.option("-path",default=MYPATH, help="指定导出的文件夹地址", type=str,prompt='Your path please')
@click.option("-text",default=None, help="指定导出的组件id", type=str,prompt='text please')
def find(path,text):
    '''
    查找一个路径下的包含关键字的的html
    '''
    find_text_in_html(path,text)


@cli.command()
@click.option("-path",default=MYPATH, help="指定导出的文件夹地址", type=str,prompt='Your path please')
@click.option("-oldtext",default=None, help="指定导出的组件id", type=str,prompt='oldtext please')
@click.option("-newtext",default=None, help="指定导出的组件id", type=str,prompt='newtext please')
def update(path,oldtext,newtext):
    '''
    替换一个路径下的所有包含关键字的html，到指定关键字
    '''
    replace_all_title(path,oldtext,newtext)
   




if __name__ == '__main__':
    
    while True:
        cli()