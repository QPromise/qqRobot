# -*- coding: utf-8 -*-
import urllib.request
import math
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
"""
网站新闻爬取
"""
def prase_web():
    url ='http://yz.ouc.edu.cn/5926/list.htm'
    #第一层循环，把url都导出来
    #定义发送的请求
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    req=urllib.request.Request(url,headers=head)
    #将服务器返回的页面放入rsp变量
    rsp = urllib.request.urlopen(req)
    #读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html = rsp.read().decode('utf-8','ignore')
    #使用BeautifulSoup模块解析变量中的web内容
    html = BeautifulSoup(html,'html.parser')
    publish_dates = html.select('.Article_PublishDate')
    # print(publish_dates)
    simple_dates = []
    for i in  range(len(publish_dates)):
        simple_dates .append(re.findall('\d.*\d',str(publish_dates[i]))[0])
    # print(simple_dates)
    info_text = ''
    info_link = ''
    new = {} # 最新的新闻
    top = {} # 置顶的新闻
    new_date = -math.inf
    count = 0
    #第二层循环，找出所有的a标签，并赋值给变量 link
    for link in html.find_all('a'):
        #把href中的内容赋值给info_link
        info_link = link.get('href')
        if re.search('page.htm',info_link):
            # print(simple_dates[count][5:7] + simple_dates[count][8:10])
            now_date = int(simple_dates[count][5:7] + simple_dates[count][8:10])
            if now_date > new_date:
                new_date = now_date
                info_text = link.get_text(strip=True)
                new = {'url':url,'info_link':info_link,'info_text':info_text,'publish_date':simple_dates[count],'real_time':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            #把a标签中的文字赋值给info_text,并去除空格
            if count == 0:
                top = {'url':url,'info_link':info_link,'info_text':info_text,'publish_date':simple_dates[0],'real_time':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            count += 1
            if count == len(simple_dates) / 2:
                break
    # print(info_text)
    # res = [top,new]
    return new
# print(prase_web())
#打印出info_text和info_link，并换行
# def check_info():
#     pre = prase_web()
#     time.sleep(1)
#     rear = prase_web()
#     print(rear)
#     if pre.get('info_text')!= rear.get('info_text'):
#         print('中国海洋大学研究生招生信息网刚刚发布了新内容！')
#         rear['flag'] = 1
#         print(rear)
#         return rear
#     else:
#         print('中国海洋大学研究生招生信息网暂时没有新动态。')
#         pre['flag'] = 0
#         print(pre)
#         return pre

