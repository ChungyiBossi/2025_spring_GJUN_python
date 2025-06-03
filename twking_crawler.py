from collections import Counter
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


# step 5: 取排行榜的交集
# from collections import Counter
top10_counter = Counter()

for booktop_name in booktop_data:
    print("Booktop: ", booktop_name)
    print("Booktop value: ")
    pprint(booktop_data[booktop_name])
    top10_counter.update(booktop_data[booktop_name])  # update top10
    print()

# 取第一名的資料，回傳(資料, 出現次數)
print('Get Top1')
pprint(top10_counter.most_common(1)[0])
top1, top1_count = top10_counter.most_common(1)[0]
top1_url, top1_name = top1
print(top1_url)
print(top1_name)
print()

# 取前三名的資料，回傳(資料, 出現次數)
print('Get Top3')
pprint(top10_counter.most_common(3))
for topn, topn_count in top10_counter.most_common(3):
    topn_url, topn_name = topn
    print(topn_url)
    print(topn_name)
