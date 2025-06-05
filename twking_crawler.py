from collections import Counter
from pprint import pprint
from bs4 import BeautifulSoup
import requests


def get_top_novels_data():
    # step 1, 2: 取回HTML
    r = requests.get('https://www.twking.org/')
    r.encoding = 'utf8'  # 處理亂碼

    # step 3: 轉化成soup
    soup = BeautifulSoup(r.text, 'html.parser')

    # step 4: 分析 - 連結 & 小說名稱 by 排行榜種類
    booktop_data = dict()  # 資料儲存
    # return list of booktops
    booktops = soup.find_all('div', class_='booktop')
    for booktop in booktops:
        booktop_name = booktop.p.string
        print(booktop_name)
        booktop_data[booktop_name] = [
            (top['href'], top.string.strip()) for top in booktop.find_all('a')
        ]  # 排行榜是key, 把[(小說連結, 書名), (小說連結, 書名) .... (小說連結, 書名)]存為value
        # TOP 10
        # for top in booktop.find_all('a'):
        #     # print(top)
        #     print(top['href'], top.string.strip())  # 連結, 小說名稱

    return booktop_data


def get_chapters(url):
    # 再更深入取得章節資訊
    r = requests.get(url)
    r.encoding = 'utf8'
    topn_soup = BeautifulSoup(r.text, 'html.parser')

    chapter_list = topn_soup.find('div', class_='info-chapters flex flex-wrap')
    chapter_count = 0  # 計算章節數目
    count_shift = 0  # 計算章節跳號數量
    for chapter in chapter_list.find_all('a'):
        # print(chapter['title'], chapter['href'])
        chapter_title = chapter['title']
        chapter_url = chapter['href']
        chapter_title_parts = chapter_title.split()  # 把章節標題用空白切開
        chapter_number = chapter_title_parts[0]  # 第幾章
        chapter_name = "".join(chapter_title_parts[1:])  # 章節名稱轉化成字串
        if chapter_number.startswith("第") and chapter_number.endswith("章"):
            print(chapter_number, '|', chapter_name, '|', chapter_url)
            chapter_count += 1
            chapter_number = int(chapter_number[1:-1])
            if chapter_number != (chapter_count + count_shift):
                print(
                    f"跳號: {chapter_count} + {count_shift} = {chapter_count+count_shift}, {chapter_number}"
                )
                count_shift += chapter_number - (chapter_count + count_shift)
                print("Update: ", count_shift)
                # break
    print("章節總數: ", chapter_count)
    print()


if __name__ == '__main__':
    # step 1~4
    booktop_data = get_top_novels_data()

    # step 5: 取排行榜的交集
    top10_counter = Counter()  # 建構子 constructor

    for booktop_name in booktop_data:
        top10_counter.update(booktop_data[booktop_name])  # update top10

    # 取前三名的資料，回傳(資料, 出現次數)
    print('Get Top3')
    pprint(top10_counter.most_common(10))
    for topn, topn_count in top10_counter.most_common(10)[7:]:
        topn_url, topn_name = topn
        # print(topn_url)
        # print(topn_name)
        get_chapters(topn_url)
