# 大量下載網路搜尋的小照片
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import base64
import os
from urllib.parse import quote_plus

# ====== 可調整參數 ======
search_query = "布偶貓"   # 替換為你想搜尋的關鍵字
scroll_times = 2          # 向下捲動次數以載入更多圖片
# =======================

# 建立「以關鍵字命名」的資料夾（自動過濾不合法字元）
def safe_dirname(name: str) -> str:
    # Windows 不允許的字元： \ / : * ? " < > | ；也去掉前後空白
    return "".join(c for c in name.strip() if c not in '\\/:*?"<>|')

images_dir = safe_dirname(search_query) if search_query else "images"
os.makedirs(images_dir, exist_ok=True)   # 若已存在就略過

# Google 圖片搜尋 URL（使用 quote_plus 以處理空白/中文）
url = f"https://www.google.com/search?hl=en&tbm=isch&q={quote_plus(search_query)}"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(5)

# 如果要更多照片就往下滑動幾次
for _ in range(scroll_times):
    driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight);')
    time.sleep(5)

images = set()  # 使用 set() 避免重複
soup = BeautifulSoup(driver.page_source, 'html.parser')
g_imgs = soup.find_all(class_="mNsIhb")
print("抓到縮圖元素數量：", len(g_imgs))

for g_img in g_imgs:
    try:
        images.add(g_img.contents[0]['src'])
    except Exception:
        pass

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
})

for idx, img_src in enumerate(images):
    file_name = os.path.join(images_dir, f'{search_query}{idx:03}.jpg')

    try:
        if img_src.startswith('data:image'):  # base64 圖片
            header, encoded = img_src.split(",", 1)
            with open(file_name, "wb") as f:
                f.write(base64.b64decode(encoded))
            print(f"Base64 下載：{file_name}")
        else:  # 直接以 URL 下載
            r = session.get(img_src, timeout=10)
            if r.status_code == 200 and r.content:
                with open(file_name, "wb") as f:
                    f.write(r.content)
                print(f"URL 下載：{file_name}")
            else:
                print(f"下載失敗（HTTP {r.status_code}）：{img_src}")
    except Exception as e:
        print("下載錯誤：", e)

# 關閉瀏覽器
driver.quit()
print(f"\n完成！圖片已存到資料夾：{images_dir}\\")
