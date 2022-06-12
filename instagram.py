from selenium import webdriver #控制 Web 瀏覽器的行為
from selenium.webdriver.common.keys import Keys #按鍵
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget
import ssl

#把證書驗證改成不需要驗證
ssl._create_default_https_context = ssl._create_unverified_context

#chromedriver路徑
path= '/usr/local/bin/chromedriver'
driver=webdriver.Chrome(path)
#step1:打開IG首頁
driver.get('https://www.instagram.com/')

#step2:登入
# 等待頁面出現name為username/password後取得標籤
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
username=driver.find_element_by_name("username")
password=driver.find_element_by_name("password")
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()

username.send_keys("username")
password.send_keys("password")
login.click()

#setp3：搜尋
WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    ) 
search=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')    
keyword=("#cat")
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)


WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    ) 
imgs = driver.find_elements_by_class_name("FFVAD")
path=os.path.join(keyword)
os.mkdir(path)
count=0
for img in imgs:
    save_as=os.path.join(path,keyword+str(count)+".jpg")
    #print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"),save_as) #wget.download(下載的位置,電腦預計存放的位置)
    count=+1