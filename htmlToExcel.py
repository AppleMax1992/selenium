from bs4 import BeautifulSoup
import re

#创建BeautifulSoup对象
bs=BeautifulSoup(open(r'C:\Users\15728\Desktop\selenium\output.html',encoding='utf-8'),features='lxml')

#获取所有文字内容
#print(soup.get_text())

#获取所有p标签的文字内容，写入TXT文件
length = len(bs.find_all("td"))
with open(r'C:\Users\15728\Desktop\selenium\test1.txt', 'w',encoding='utf-8') as f:
    for item in bs.find_all("tr"):
        # print(item)
        tddata = item.find_all('td')
        print(tddata[1].text)
        
        f.write(str(tddata[1].text)+'\n')