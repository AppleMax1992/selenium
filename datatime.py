# # coding:utf-8
# import requests
# from bs4 import BeautifulSoup
# cookie = '''PHPSESSID=f2nudui3nm25qfjpprk56g07fl'''

# header = {    
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',    
# 'Connection': 'keep-alive',       
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',  
# 'Cookie': cookie}

# url = 'https://qc.qichenglantai.com/approval/detail/id/2545416.html'
# wbdata = requests.get(url,headers=header)

# #start
# soup = BeautifulSoup(wbdata.text,'html.parser')
# # print(soup)
# page = soup.findAll('input')

# print(page)


from selenium import webdriver

# driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument("--headless")  # 无界面
# options.add_argument('--disable-gpu')
# options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(executable_path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=options)
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"')
options.add_argument('Connection="keep-alive"')
options.add_argument('accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"')
driver.maximize_window()
# options.add_argument('Cookie="PHPSESSID=35u9m14aqo4hjt38e2p1sgorps"')

driver.get("https://qc.qichenglantai.com/approval/detail/id/2545416.html")
driver.add_cookie({"name": "PHPSESSID", "value": "35u9m14aqo4hjt38e2p1sgorps"})
driver.refresh() # 刷新方法 refresh
driver.get("https://qc.qichenglantai.com/approval/detail/id/2545416.html")
# 收件日期
# storage_start_date = driver.find_element_by_name("storage_start_date")
# l=driver.find_element_by_xpath("//h1/following-sibling::h2")
storage_start_date =  driver.find_element_by_xpath("//input[@name='storage_start_date']/following-sibling::span").text
create_time  = driver.find_element_by_xpath("//div[@user_id='144']/span")

print("===================",storage_start_date)
# print(create_time.text)
# create_time.click()
# span.send_keys(i)
# create_time.__setattr__("text","aaaa")
driver.execute_script("arguments[0].innerText ='"+ storage_start_date+"'", create_time)
# print("===================",create_time.send_keys(storage_start_date.text))
# Adds the cookie into current browser context
