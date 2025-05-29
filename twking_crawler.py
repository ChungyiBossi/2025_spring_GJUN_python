from pprint import pprint
from bs4 import BeautifulSoup
import requests

# step 1, 2: 取回HTML
r = requests.get('https://www.twking.org/')
r.encoding = 'utf8'  # 處理亂碼
print(r.text)

# step 3: 轉化成soup
soup = BeautifulSoup(r.text, 'html.parser')

# step 4: 分析 - 連結 & 小說名稱 by 排行榜種類
booktop_data = dict()  # 資料儲存
booktops = soup.find_all('div', class_='booktop')  # return list of booktops
for booktop in booktops:
    booktop_name = booktop.p.string
    print(booktop_name)
    booktop_data[booktop_name] = [
        (top['href'], top.string.strip()) for top in booktop.find_all('a')
    ]  # 排行榜是key, 把[(小說連結, 書名), (小說連結, 書名) .... (小說連結, 書名)]存為value
    # TOP 10
    for top in booktop.find_all('a'):
        # print(top)
        print(top['href'], top.string.strip())  # 連結, 小說名稱

pprint(booktop_data)
