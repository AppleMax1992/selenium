from selenium import webdriver
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
options = Options()
driver = webdriver.Chrome(executable_path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=options)
# options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"')
# options.add_argument('Connection="keep-alive"')
# options.add_argument('accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"')
driver.maximize_window()

# 一定要打开网页之后再加载cookie
driver.get("https://qc.qichenglantai.com/publics/login.html")
driver.add_cookie({"name": "PHPSESSID", "value": "35u9m14aqo4hjt38e2p1sgorps"})
# driver.refresh() # 刷新方法 refresh
driver.get("https://qc.qichenglantai.com/approval/detail/id/2545416.html")
# 收件日期
storage_start_date =  driver.find_element(By.XPATH,"//input[@name='storage_start_date']/following-sibling::span").text
# 收到签字日期
create_time  = driver.find_element(By.XPATH,"//div[@user_id='144']/span")
# 写入
driver.execute_script("arguments[0].innerText ='"+ storage_start_date+"'", create_time)
