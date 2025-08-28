# 大量下載網路搜尋的小照片
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import base64

search_query = "布偶貓"  # 替換為你想搜尋的關鍵字
# Google 圖片搜尋 URL
url = f"https://www.google.com/search?hl=en&tbm=isch&q={search_query}"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(5)

# 如果要更多照片就往下滑動幾次
for n in range(2):
    driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight);')
    time.sleep(5)

images = set()  # 使用 set() 避免重複
soup = BeautifulSoup(driver.page_source, 'html.parser')
g_imgs = soup.find_all(class_="mNsIhb")
print(len(g_imgs))

for g_img in g_imgs :
    images.add(g_img.contents[0]['src'])

for idx, img_src in enumerate(images):
    file_name = f'./cats_img/cat{str(idx).zfill(3)}.jpg'
    if img_src.startswith('data:image'):  # base64 圖片
        header, encoded = img_src.split(",", 1)
        # 解碼 base64 字串
        # 將解碼後的資料寫入檔案
        with open(file_name, "wb") as f:
            f.write(base64.b64decode(encoded))
        print(0)
    else:  # URL 下載
        response = requests.get(img_src)
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(1)
