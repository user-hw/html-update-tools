#conding=utf8  
from common import getAllHtml ,hasText,replace_title


def find_text_in_html(mypath,text):
    '''
    1.查找所有的包含关键字的html，返回路径
    input：根目录，关键字
    output：路径列表
    '''
    htmlList = getAllHtml(mypath)
    res = []
    for html in htmlList:
        if hasText(html,text):
            res.append(html)
    return res

def replace_all_title(mypath,oldName,newName):
    '''
    2.替换所有标题里的关键字
    input：根目录，原来的关键字，新的关键字
    output：T/F
    '''
    htmlList = getAllHtml(mypath)
    # for html in htmlList:
    #     print(html)
    # return 
    for html in htmlList:
        try:
            replace_title(html,oldName,newName)

        except Exception as ex:
            print(html+' 操作失败')
            print("出现如下异常%s"%ex)
            
    return True
# replace_all_title(mypath,'雪浪','新的标题')
    
    