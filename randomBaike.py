import random
import re
#import datetime#也可以用当前时间作为种子输入
from urllib.request import urlopen
from bs4 import BeautifulSoup

random.seed(1231241231)#这里采用的种子

def getLinks(articleUrl):
    html=urlopen('https://baike.baidu.com{}'.format(articleUrl))
    bs=BeautifulSoup(html,'html.parser')
    name=(bs.find('dd',{'class':'lemmaWgt-lemmaTitle-title'}).find('h1'))
    print(name.get_text())
    return bs.find('div',{'class':'lemma-summary'}).find_all('a',href=re.compile('^(/item/)'))

links=getLinks('/item/JOJO%E7%9A%84%E5%A5%87%E5%A6%99%E5%86%92%E9%99%A9/4422729')
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs['href']
    links=getLinks(newArticle)