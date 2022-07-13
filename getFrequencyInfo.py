# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pandas as pd
from urllib import request
import urllib.parse
import requests
# import socket
options = Options()
# options.add_argument("--headless")  # 无界面
driver = webdriver.Chrome(executable_path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=options)
# socket.setdefaulttimeout(100)
#下载网页内容
def html_download(url):
        if url is None:
            return None
        try:
#        r = requests.get(url, timeout=30)headers=headers
#        return r.status_code
        #timeout表示如果30s没有返回，就抛出一个规定时间未返回异常
            headers = {'User-Agent':'Mozilla/5.0'}
            r = requests.get(url, headers = headers)
            r.raise_for_status()#如果状态不是200，引发HTTPError异常
            r.encoding = 'utf-8' #apparent_encoding
            
            return r.text
        #网络连接有风险，抛出错误异常
        except:
            return "--获取页面异常--"

def getfirstTimePageDriver(url):
    # print(url)
    # try:/
    try:
        driver.get(url)
        
        driver.refresh() # 刷新方法 refresh
    # 进入第二页
    # 如果有翻页
    
        element = driver.find_element_by_class_name('pTag.last')
    
        # viewTime = element.text
        # 跳转到最后一页
        element.click()
        # print(aElement)
        # except:
        #     print('没有浏览次数')

        # 只要数字
        # 加r说明不要转义
        # editedTimes = re.sub(r'\D','',getTotalEdit(driver))
        lastTime = getlastTable(driver)
        # print(lastTime)
    except:
        lastTime = None
        # print('except')
    # print(viewTime)
    # print(editedTimes)
    # content.append(editedTimes)
    # driver.quit()
    return lastTime
# 把页面点到没有下一页为止



def getlastTable(dr):
    time.sleep(2)
    table =  dr.find_element_by_class_name('versionList')
    # 所有row的
    # print(table)
    all_rows = table.find_elements_by_tag_name("tr") 
    # for col in all_rows[-1]:
        # cells = .find_elements_by_tag_name("td")
    # 在最后一行里找所有的td
    cols = all_rows[-1].find_elements_by_tag_name("td")
    # print('=============',cols[0].text)
    return cols[0].text

def getTotalViewTime(url):
    # encodeName = urllib.parse.quote(keyword)
    # url = "https://baike.baidu.com/search/word?word=" + encodeName
    # redirectUrl = request.urlopen(url).geturl()
    # print(redirectUrl)
    time.sleep(2)
    try:
        soup = BeautifulSoup(html_download(url), 'html.parser')
        TotalViewTime = soup.find('span', id_='j-lemmaStatistics-pv').text
        TotalViewTime = re.findall(r"\d+", TotalViewTime)[0]
    except:
        TotalViewTime = None
    print(TotalViewTime)
    return TotalViewTime
def getFirstTime(url):
    # print(url)
    try:
        soup = BeautifulSoup(html_download(url), 'html.parser')
        table = soup.find('tbody')
        # print(table)
        all_rows = table.find_all("tr") 
        # print(all_rows)
        firstRow = all_rows[0]
        # print('==================',all_rows[1])
        cells = firstRow.find_all("td")
        # print(cells)
        cells = cells[0].text
        
    except:
        cells = None
    # print(cells)
    return cells

def historySearch(keyword):
#根据关键词定位到词条的历史编辑链接
    # print(keyword)
    encodeName = urllib.parse.quote(keyword)
    url = "https://baike.baidu.com/search/word?word=" + encodeName
    keep_request = True
    while keep_request:
        try:
            redirectUrl = request.urlopen(url,timeout=10).geturl()
            # print(redirectUrl)
            soup = BeautifulSoup(html_download(redirectUrl), 'html.parser')
            #返回第一个结果,有待验证
            # print(soup)
            history = soup.find('a', class_='nslog:1021')
            # print(history)
            if(history == None) :
                # print()
                # 有多个选项
                try:
                    url = soup.find_all('div', class_='para')
                    # print(url[0])
                    a = url[0].find('a')
                    # print(a['href'])
                    url = 'https://baike.baidu.com' + a['href']
                    # print(url)
                    redirectUrl = request.urlopen(url,timeout=10).geturl()
                    soup = BeautifulSoup(html_download(redirectUrl), 'html.parser')
                    history = soup.find('a', class_='nslog:1021')
                except:
                    historyUrl = None
            keep_request = False
        except :
            # 遇到错误，等待
            time.sleep(1)
    try:
        historyUrl = 'https://baike.baidu.com'+ history['href']
    except:
        historyUrl = None
    return historyUrl

# historySearch('胡锦涛') 



#根据关键词定位到词条的百科链接
def Search(keyword):
    # print(keyword)
    encodeName = urllib.parse.quote(keyword)
    url = "https://baike.baidu.com/search/word?word=" + encodeName
    keep_request = True
    # print(url)
    while keep_request:
        try:
            baikeUrl = request.urlopen(url,timeout=10).geturl()
            # print('我是url', baikeUrl)
            soup = BeautifulSoup(html_download(baikeUrl), 'html.parser')
            # if(baikeUrl == None) :
            #     print()
            #     # 有多个选项
            #     try:
            #         url = soup.find_all('div', class_='para')
            #         # print(url[0])
            #         a = url[0].find('a')
            #         print(a['href'])
            #         url = 'https://baike.baidu.com' + a['href']
            #         print(url)
            #         baikeUrl = request.urlopen(url,timeout=10).geturl()
            #         # soup = BeautifulSoup(html_download(redirectUrl), 'html.parser')
            #         # viewTimes = soup.find('span', id_='j-lemmaStatistics-pv')
            #     except:
            #         baikeUrl = None
            keep_request = False
        except :
            # 遇到错误，等待
            time.sleep(1)
    # try:
    #     baikeUrl = 'https://baike.baidu.com'+ history['href']
    # except:
    #     baikeUrl = None
    return baikeUrl


def readExcel():
    f = open('test1.txt',encoding='utf-8')
    data = f.readlines()
    f.close()
    return data

def getViewTimes(datas):
    it = iter(datas)
    # print(datas)
    # # r = open("total.txt","a",encoding='utf-8')   #设置文件对象
    for data in it:
        baikeUrl = Search(data)
        # del line
        r = open("viewTimes.txt","a",encoding='utf-8')   #设置文件对象
        # times = getTotalViewTime(baikeUrl)
        # times = pageDriver(baikeUrl)
        # times = Search(data)
        # r.write(str(times) + '\n')
        r.close()

def gethistoryLastTimes(datas):
    it = iter(datas)
    # print(datas)
    # # r = open("total.txt","a",encoding='utf-8')   #设置文件对象
    for data in it:
        # print(data)
        historyUrl = historySearch(data)
        # del line
        # print(historyUrl)
        r = open("historyTimes.txt","a",encoding='utf-8')   #设置文件对象
        # times = getTotalViewTime(baikeUrl)
        times = getFirstTime(historyUrl)
        print(times)
        # times = Search(data)
        r.write(str(times) + '\n')
        r.close()
def gethistoryFirstTimes(datas):
    it = iter(datas)
    # print(datas)
    # # r = open("total.txt","a",encoding='utf-8')   #设置文件对象
    for data in it:
        # print(data)
        historyUrl = historySearch(data)
        # del line
        # print(historyUrl)
        # times = getTotalViewTime(baikeUrl)
        times = getfirstTimePageDriver(historyUrl)
        print(times)
        # times = Search(data)
        # driver.quit()
def getTotalEdit(datas):
    it = iter(datas)
    # print(datas)
    # # r = open("total.txt","a",encoding='utf-8')   #设置文件对象
    for data in it:
        historyUrl = historySearch(data)
        # print(historyUrl)
        try:
            soup = BeautifulSoup(html_download(historyUrl), 'html.parser')
            editedTimes = soup.find('div', class_='editedTimes').text
            # print('historyUrl', editedTimes)
            editedTimes = re.findall(r"\d+", editedTimes)[0]
        except:
            editedTimes = None
        print(editedTimes)
        # return editedTimes

def main():
    # data = readExcel()
    # write_file = "path_to_file.xlsx"
    # #data = (1,2,3)
    # # print(data)
    # df = pd.DataFrame(index =[0])
    # # print(df)   
    
    # for item in data:
    #     item = item.splitlines()
    #     historyUrl = historySearch(item[0])
    #     #    print(historyUrl)
    #     contentList = []
    #     try:
    #         content = pageDriver(historyUrl)
    #     except:
    #         content = None
    #     contentList.append(content)
    #     df = df.append(contentList,ignore_index=True)
    #     print('============df===============',df)
    # df.to_excel(write_file)
    # pageDriver('https://baike.baidu.com/historylist/Uliweb/3705838')
        # historyUrl = historySearch('特朗普')
        # times = getFirstTime(historyUrl)
    # f = open("test1.txt","r",encoding='utf-8')   #设置文件对象
    # datas = []
    # for line in f:
    #     line = line[:-1]
    #     datas.append(line)
    datas = ['北京','陈卓璇', '皓嫣', '南京', '肖战', '吴磊', '苏醒', 'FPX', '陈祥榕', '西藏', '中尼', '美', '陈建斌', '安徽商场', '上海', '台', '杜兰特', '张哲瀚', '唱会', '尹正', '河南女排', '辽宁女排', '河', 'RNG', '好利来', '李宁', '长城', '刘诗诗', '张艺兴', '秦海璐', '霸', '林芸芸', '尼日利亚', '蒋勤勤', '八达岭', '内蒙古', '解放军', '中国', '赵立坚', '山', '张雨绮', '吉濑美智子', '王嘉尔', '朱婷', 'by']
    # getViewTimes(datas)
    # gethistoryLastTimes(datas)
    # getTotalEdit(datas)
    gethistoryFirstTimes(datas)
        # f.close() #关闭文件
main()

# pageDriver('https://baike.baidu.com/historylist/%E4%B8%AD%E5%8D%97%E5%A4%A7%E5%AD%A6/143850')