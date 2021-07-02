import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import re
import xlrd
options = Options()
# options.add_argument("--headless")  # 无界面
# options.add_argument('--disable-gpu')
# options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(executable_path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=options)
startUrl = 'https://qc.qichenglantai.com'
# url = 'https://qc.qichenglantai.com/create_table/add.html?id=2206&type=4&template_id=625&s_id=2701&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?138-1991-2206'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604972b70005c&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?138-1990-2207'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604c8bb03abeb&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?138-1993-2428'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604a0d4b183d7&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?138-1996-112'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=6050271c7eb5f&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?138-1996-2334'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604ae6a51aa93&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1961-2346'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604b710f32743&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1961-2369'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604b28b136eec&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1964-2352'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604b605154adb&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1964-2363'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604b8217b7375&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1964-2378'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604c16eb9de63&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1964-2390'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604c34f01311e&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1964-2401'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604c6b9b322d7&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?139-1964-2414'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=6050012274a02&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1848-2631'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=60500d1618d99&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1848-2638'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=605065717cd25&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1848-2663'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=605066066ac89&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1848-2666'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=6050666402ee5&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1848-2669'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=60504ca14fe79&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1848-2652'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604da56689466&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1852-2484'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=6050676e50729&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1852-2672'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604db6adb5fe5&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1858-2529'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604ed075c2c03&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1858-2594'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604ed36a43a2c&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1771-2596'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604f199a8a5f6&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1771-2613'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604dbe102eaac&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1774-2536'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604dd2172272a&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1774-2547'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604dfe5db27ec&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1774-2559'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604e17de2f10e&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1774-2562'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604ea66fe5038&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1774-2567'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604eb9ec8aae7&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?133-1774-2579'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=604d66f7efa63&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/41/type/1.html?138-1993-2449'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=6050012274a02&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/37/type/1.html?132-1848-2631'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=60593fb7442d3&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/33/type/1.html?114-1043-2796'
#print(res.text)
# url ='https://qc.qichenglantai.com/create_table/edit.html?uniqid=605a9067495f3&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/33/type/1.html?114-1043-2911'
# url ='https://qc.qichenglantai.com/create_table/edit.html?uniqid=6059a36687854&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/33/type/1.html?114-1046-2808'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=6059892ccc870&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/33/type/1.html?114-1046-2897'
# url ='https://qc.qichenglantai.com/create_table/edit.html?uniqid=605aede183d3f&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/33/type/1.html?114-1046-2926'
# url = 'https://qc.qichenglantai.com/create_table/edit.html?uniqid=60d5f720b6f0f&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/24/type/1.html?90-3469-15824'
# url ='https://qc.qichenglantai.com/create_table/add.html?id=13585&type=4&template_id=624&s_id=2725&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/24/type/1.html?90-3472-13585'
url = 'https://qc.qichenglantai.com/create_table/add.html?id=13585&type=4&template_id=628&s_id=2726&data-url=https://qc.qichenglantai.com/engineering/indexlist/id/24/type/1.html?90-3472-13585'
#下载网页内容
driver.maximize_window()
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
def findImg(ele):
    # sleep(2)
    text_img_divs = ele.find_elements_by_class_name('text-img')
    arr = [0,0,0,0]
    i = 0
    j = 0
    for text_img_div in text_img_divs:
      span = text_img_div.find_element_by_tag_name('span')
      if span.text !='':
        arr[i%4] = span.text
        i = i + 1
        # print(arr[0])
        j = 10
      elif (span.text == '') and (j > 0) :
        j = j - 1
        
        arr3 = arr[3][1:].split(",")
        # print('1111111', int(re.findall(r"\d+\.?\d*",'-10')[0]))
        # re.findall(r"\d+\.?\d*",arr3[1])
        num = random.randint(int(re.findall(r"\d+\.?\d*",arr3[1])[0]),int(arr3[0])) if len(arr3) >1 else arr3[0]
        # print(num)
        span.click()
        span.send_keys(random.randint(int(arr[2])-int(num),int(arr[2])+int(num)))

def readExcel(path):
  data = xlrd.open_workbook(path)
  table = data.sheet_by_name('Sheet1')
  # print(table.row_values(22))
  # table.cell(i,j).value
  return table


def find_jiaozhu(ele):
    row_arr = []
    path = './混凝土浇筑施工记录表.xlsx'
    table = readExcel(path)
    i = 0
    while i < 15 :
      i = i + 1
      row_arr.append(table.row_values(i))
    print(row_arr)

    text_img_divs = ele.find_elements_by_class_name('text-img')
    start = 1
    for index, text_img_div in enumerate(text_img_divs):
      span = text_img_div.find_element_by_tag_name('span')
      # print(span.text)
      span.click()
      # span.send_keys(start)
      # start = start + 1
      if index == 18:
        # 施工日期开始
        span.send_keys('3.30 14:15')
      if index == 19:
        # 施工日期结束
        span.send_keys('3.30 18:30')
      if index == 0:
        # 施工气温最高
        span.send_keys('最高11°C')
      if index == 1:
        # 施工气温最低
        span.send_keys('最低1°C')
      if index == 2:
        # 设计配合比
        span.send_keys(row_arr[4][1])
      if index ==3:
        # 运输方式
        span.send_keys(row_arr[5][1])
      if index ==4:
        # 入模方式
        span.send_keys(row_arr[6][1])
      if index ==5:
        # 混凝土强度等级
        span.send_keys(row_arr[4][6])
      if index ==6:
        # 振捣方式
        span.send_keys(str(row_arr[5][6]))
      if index ==7:
        # 实测塌落度
        span.send_keys(str(row_arr[7][1]))
      if index ==8:
        span.send_keys(str(row_arr[7][3]))
      if index == 9:
        span.send_keys(str(row_arr[7][5]))
      if index == 10:
        # 平均
        span.send_keys(str(row_arr[7][7]))
      if index == 11:
        # 留取样式 组数
        span.send_keys(str(row_arr[8][2]))  
      if index == 12:
        # 编号
        span.send_keys(str(row_arr[8][4]))
      if index ==13:
        # 设计方式
        span.send_keys(str(row_arr[9][1]))
      if index ==14:
        # 实浇方数
        span.send_keys(str(row_arr[9][6]))
      if index ==15:
        # 养护方式及措施
        span.send_keys(str(row_arr[11][1]))
      if index ==16:
        # 施工间断情况记录
        span.send_keys(str(row_arr[12][1]))
      if index == 17:
        # 发现问题
        span.send_keys(str('无'))



def findHunningtu(ele):
    row_arr = []
    path = './混凝土拌和运输施工记录表.xlsx'
    table = readExcel(path)
    i = 0
    while i < 22 :
      i = i + 1
      row_arr.append(table.row_values(i))

    print(row_arr)



    text_img_divs = ele.find_elements_by_class_name('text-img')
    start = 1
    for index, text_img_div in enumerate(text_img_divs):
      span = text_img_div.find_element_by_tag_name('span')
      print(span.text)
      span.click()
        # 对于前4行，横着找
      
      # if(start<5):
      #   print(row_arr[start][8])
      #   start = start + 1
      if index == 57:
        # 施工日期
        span.send_keys('2021年3月30日')
        
      if index == 0:
        # 设计混凝土强度
        span.send_keys(row_arr[2][8])
      if index == 1:
        # 施工天气
        span.send_keys(row_arr[3][2])
      if index == 2:
        # 设计塌落度
        span.send_keys(row_arr[3][8])
      if index ==3:
        # 规格品种
        span.send_keys(row_arr[6][3])
      if index ==4:
        # 材料产地
        span.send_keys(row_arr[8][3])
      if index ==5:
        # 含水量
        span.send_keys('/')
      if index ==6:
        # 实验室配合比
        span.send_keys(str(row_arr[10][3]))
      if index ==7:
        # 施工配合比
        span.send_keys(str(row_arr[11][3]))
      if index ==8:
        # 每盘拌合量
        span.send_keys(str(row_arr[12][3]))
      if index == 9:
        span.send_keys(str(row_arr[6][4]+row_arr[7][4]))
      if index == 10:
        span.send_keys(str(row_arr[8][4]))
      if index == 11:
        span.send_keys(str(row_arr[9][4]))  
      if index == 12:
        span.send_keys(str(row_arr[10][4]))
      if index ==13:
        span.send_keys(str(row_arr[11][4]))
      if index ==14:
        span.send_keys(str(row_arr[12][4]))
      if index ==15:
        span.send_keys(str(row_arr[6][5]))
      if index ==16:
        span.send_keys(str(row_arr[8][5]))
      if index ==17:
        span.send_keys(str(row_arr[9][5]))
      if index == 18:
        span.send_keys(str(row_arr[10][5]))
      if index == 19:
        span.send_keys(str(row_arr[11][5]))
      if index == 20:
        span.send_keys(str(row_arr[12][5]))
      if index ==21:
        span.send_keys(str(row_arr[6][6]))
      if index ==22:
        span.send_keys(str(row_arr[8][6]))
      if index ==23:
        span.send_keys(str(row_arr[9][6]))
      if index == 24:
        span.send_keys(str(row_arr[10][6]))
      if index == 25:
        span.send_keys(str(row_arr[11][6]))
      if index == 26:
        span.send_keys(str(row_arr[12][6]))
      if index ==27:
        span.send_keys(str(row_arr[6][7]))
      if index ==28:
        span.send_keys(str(row_arr[8][7]))
      if index ==29:
        span.send_keys(str(row_arr[9][7]))
      if index == 30:
        span.send_keys(str(row_arr[10][7]))
      if index == 31:
        span.send_keys(str(row_arr[11][7]))
      if index == 32:
        span.send_keys(str(row_arr[12][7]))
      if index ==33:
        span.send_keys(str(row_arr[6][9]))
      if index ==34:
        span.send_keys(str(row_arr[8][9]))
      if index ==35:
        span.send_keys(str(row_arr[9][9]))
      if index == 36:
        span.send_keys(str(row_arr[10][9]))
      if index == 37:
        span.send_keys(str(row_arr[11][9]))
      if index == 38:
        span.send_keys(str(row_arr[12][9]))
      if index ==39:
        span.send_keys(str(row_arr[6][10]))
      if index ==40:
        span.send_keys(str(row_arr[8][10]))
      if index ==41:
        span.send_keys(str(row_arr[9][10]))
      if index == 42:
        span.send_keys(str(row_arr[10][10]))
      if index == 43:
        span.send_keys(str(row_arr[11][10]))
      if index == 44:
        span.send_keys(str(row_arr[12][10]))
      if index == 45:
        span.send_keys(str(row_arr[14][3]))
      if index ==46:
        span.send_keys(str(row_arr[15][3]))
      if index ==47:
        span.send_keys(str(row_arr[16][3]))
      if index == 48:
        span.send_keys(str(row_arr[17][3]))
      if index == 49:
        span.send_keys(str(row_arr[18][3]))
      if index == 50:
        span.send_keys(str(row_arr[14][8]))
      if index ==51:
        span.send_keys(str(row_arr[15][8]))
      if index ==52:
        span.send_keys(str(row_arr[16][8]))
      if index == 53:
        span.send_keys(str(row_arr[17][8]))
      if index == 54:
        span.send_keys(str(row_arr[18][8]))
      if index == 55:
        span.send_keys(str(row_arr[19][3]))
def pageDriver(url):
    print(startUrl)
    # try:/
    driver.get(startUrl)
    driver.add_cookie({'name' : 'PHPSESSID', 'value' : 'e2pi5j3hkq9ra0do9itmgdr9mg'})
    
    # driver.add_argument('--headless')
    driver.refresh() # 刷新方法 refresh
    driver.get(url)

    # # driver.add_cookie({'name':'dv6lc67iicq47tih23prmn0147'})
    gImg = driver.find_elements_by_id('imgDiv')
    ImgDiv = gImg
    # print(ImgDiv)
    # print(gImg[1:-1])
    for item in ImgDiv :
      print(item)
      # 钢筋安装检验报告
      # findImg(item)
      # 混凝土拌和运输施工记录表
      # findHunningtu(item)
      # 混凝土浇筑施工记录表
      find_jiaozhu(item)
    # element = driver.find_element_by_id('imgDiv3')


    #   span.click()
    #   span.send_keys(1)
    # viewTime = element.text
        # aElement.click()
    # print(aElement)
    # except:
    #     print('没有浏览次数')

    # 只要数字
    # 加r说明不要转义
    # editedTimes = re.sub(r'\D','',getTotalEdit(driver))
    # lastPageTable = getlastTable(driver)
    # print(lastPageTable)
    # lastTime = lastPageTable[-6].text
    # print(spans)
    # print(editedTimes)
    # content.append(editedTimes)
    # driver.quit()
    # return viewTime
pageDriver(url)