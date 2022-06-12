# Python爬蟲程式碼
此專案主要放置Python爬蟲程式碼
## Instagram爬蟲程式（instagram.py）
此程式是利用selenium 網頁自動化，操控瀏覽器Chrome登入Instagram後，搜尋關鍵字獲得相關貼文。
## Dcard爬蟲程式（dcard.py）
此程式利用selenium 網頁自動化，操控瀏覽器Chrome在Dcard搜尋”比特幣”相關發文後，進入文章內容。
## Googlemap爬蟲程式（googlemap.py）
此程式利用發送GET請求取得資料後轉換為JSON格式，再將資料進行處理切割。程式執行完後會整理出以下資料欄位：
* 品牌
* 分店
* 地址
* lat
* lng
* 日期
* 評論內容
* 評分星數
## 日文學習網站gogakuru爬蟲程式（gogakuru.py）
此程式利用selenium 網頁自動化，抓取網頁中所有英文句子，並存成以下三種形式：
1. txt
1. 直接串資料庫存入
1. pickle 

