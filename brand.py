from selenium import webdriver
from lxml import etree
import time
#导入类 实现让selenium规避被检测到的风险
from selenium.webdriver import ChromeOptions
#实现让selenium规避被检测到的风险
option=ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#加载谷歌驱动程序
bro=webdriver.Chrome('./chromedriver')
#对当前页面发起请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
time.sleep(2)
#获取当前页面数据
page_text=bro.page_source
#将页面数据存储到列表中
all_page_text=[page_text,]
#实例化一个tree对象 进行数据解析
tree=etree.HTML(page_text)
#数据解析 定位标签属性
detail_url=tree.xpath('//ul[@id="gzlist"]/li/dl/a/@href')
print(len(detail_url))
# print(detail_url)
for url in detail_url:
    #对详情页发起请求
    bro.get(url)
    time.sleep(3) #让页面停留好进行数据爬取（这个必需要有，没有会报错）
    # print(url)
    #获取当前页源码
    detail_page_text=bro.page_source
    #存储页面源码
    all_detail_page_text=[detail_page_text]
    #数据解析
    tree=etree.HTML(detail_page_text)
    #定位到标签属性
    tr_list=tree.xpath('/html/body/div[4]/table/tbody/tr')
    print(len(tr_list))
    for k,tr in enumerate(tr_list):
        if(k == 0):
          name = tr.xpath('./td/text()')[0]
          time.sleep(1) #可要可不要
          try:
              name1 = tr.xpath('./td[2]/text()')[0]
              time.sleep(2)
              print(name1)
          except:
              print('Error')
          print("name",name)

time.sleep(2)
bro.close()
