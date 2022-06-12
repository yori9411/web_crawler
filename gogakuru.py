from selenium import webdriver
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pandas as pd
import pickle
import time
import mysql.connector

# 驅動程式前的相關設定
UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless") # 隱藏瀏覽器畫面
chrome_options.add_argument("--no-sandbox") # 以最高權限運行
chrome_options.add_argument("user-agent=" + UserAgent)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://gogakuru.com/english/phrase/genre/180_初級レベル.html?layoutPhrase=1&orderPhrase=1&condMovie=0&flow=enSearchGenre&condGenre=180&perPage=50")

# 需等待一段時間讓JS順利完成渲染,讓程式可以順利抓到網頁渲染完成後的結果
time.sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')

#抓網站中的句子
word_soup = soup.find_all('span',{'class':'font-en'}) 
all_word=[]
for item in word_soup:
  all_word.append(item.text)
final_word='\n'.join(all_word)

#寫入txt檔
with open("word.txt","w",encoding="utf-8") as f:
  f.write(final_word)

#寫入pickle
with open('word.pickle', 'wb') as f:
    pickle.dump(final_word, f) 

#dataframe寫入db
df = pd.DataFrame({'Phrase': all_word})
 
try:
    # MySQL的使用者：root, 密碼:, port：3306, 資料庫：db_name
    engine = create_engine('mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db_name}?charset=utf8'.format(
        user='root',
        pwd='',
        host='127.0.0.1',
        port='3306',
        db_name='db_name',
    ),
        encoding='utf-8',
    )
    # if_exists='append' -> 如果表格存在，把資料插入，如果不存在就創建一個表格 
    df.to_sql('table_name', engine, if_exists='append', index=False)
    engine.dispose() # 關閉資料庫連線
    print("寫入成功")
except:
    print("寫入失敗")