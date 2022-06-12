from selenium import webdriver #控制 Web 瀏覽器的行為
from selenium.webdriver.common.keys import Keys #按鍵
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#chromedriver路徑
path= '/usr/local/bin/chromedriver'
driver=webdriver.Chrome(path)
#打開dcard首頁
driver.get('https://www.dcard.tw/f')

# #取得網頁title
print(driver.title)

#於搜尋欄內輸入比特幣
search=driver.find_element_by_name("query")
search.clear() #清空搜尋欄位
search.send_keys("比特幣")
#按下enter鍵
search.send_keys(Keys.RETURN)
#按下enter後頁面跳轉需要時間，出現CLASS_NAME＝sc-3yr054-1後才繼續執行
WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
    ) 
    
#印出搜尋後的文章標題    
titles=driver.find_elements_by_class_name("tgn9uw-3")
for title in titles:
    print(title.text)

#取得連結並點擊
link=driver.find_element_by_link_text("#分享 勸世文 千萬不要碰當沖")
link.click()
driver.back() #瀏覽器回到上一頁
driver.forward() #瀏覽器回到下一頁
#5秒後關閉
time.sleep(5)
#關閉網頁
driver.quit() 