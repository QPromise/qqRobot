#coding=utf-8

import urllib.request
from bs4 import BeautifulSoup
import re
import time
def prase_web():
    url ='http://yz.ouc.edu.cn/5926/list.htm'
    #第一层循环，把url都导出来
    #定义发送的请求
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
    req=urllib.request.Request(url,headers=head)
    #将服务器返回的页面放入rsp变量
    rsp = urllib.request.urlopen(req)
    #读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html = rsp.read().decode('utf-8','ignore')
    #使用BeautifulSoup模块解析变量中的web内容
    html = BeautifulSoup(html,'html.parser')
    info_text = ''
    info_link = ''
    #第二层循环，找出所有的a标签，并赋值给变量 link
    for link in html.find_all('a'):
        #把href中的内容赋值给info_link
        info_link = link.get('href')
        if re.search('page.htm',str(info_link)):
            #print(info_link)
            #把a标签中的文字赋值给info_text,并去除空格
            info_text=link.get_text(strip=True)
            break
    #print(info_text)
    res = {'url':url,'info_link':info_link,'info_text':info_text}
    return res
#打印出info_text和info_link，并换行
def check_info():
    pre = prase_web().get('info_text')
    time.sleep(30)
    ans = {}
    if pre!= prase_web().get('info_text'):
        print('中国海洋大学研究生招生信息网刚刚发布了新内容！')
        ans = prase_web()
        ans['flag'] = 1
        print(ans)
        return ans
    else:
        print('中国海洋大学研究生招生信息网暂时没有新动态。')
        ans = prase_web()
        ans['flag'] = 0
        print(ans)
        return ans

