# Google 圖片下載程式 

## 專案簡介
這是一個練習用的 Python 專案，透過 **Selenium** 與 **BeautifulSoup**，自動批量下載 Google 圖片。  
目前的搜尋關鍵字預設為「布偶貓」，你可以自行修改程式中的 `search_query` 變數來搜尋其他圖片。  

⚠️ 本程式僅供學習與研究使用，下載的圖片可能涉及版權，請勿用於商業用途。

---

##  功能特色
- 自動開啟 Google 圖片搜尋
- 批量下載搜尋結果中的圖片
- 支援 Base64 圖片與一般圖片 URL 下載
- 自動下滑頁面，載入更多圖片

---

##  使用方法

### 1 安裝必要套件
請先安裝 Python 3.x，並在終端機輸入以下指令：

pip install selenium beautifulsoup4 requests


### 2 設定 ChromeDriver

* 需要安裝與你 Chrome 瀏覽器版本相符的 **ChromeDriver**
* 下載網址：[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
* 下載後將 `chromedriver.exe` 放到程式可執行的路徑，或放在與 `main.py` 同一資料夾

### 3 執行程式

main.py

### 4 修改搜尋關鍵字

在 main.py 中修改：


search_query = "布偶貓"

即可下載不同主題的圖片。

---

##  專案結構


.
├── main.py          # 主程式
├── README.md        # 專案說明文件
├── LICENSE          # MIT 授權
├── .gitignore       # 忽略不必要上傳的檔案
└── cats_img/        # 下載下來的圖片將儲存在這裡


---

##  範例

執行後會在 `cats_img/` 資料夾中看到類似這樣的圖片：

```
cat000.jpg
cat001.jpg
cat002.jpg
...
```

---

## 授權

此專案以 **MIT License** 授權，歡迎自由使用、修改與分享，但請勿將下載的圖片用於商業用途。
