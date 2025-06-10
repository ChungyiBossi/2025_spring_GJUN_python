from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# 初始化參數
page_size = 500
current_page = 1
driver = webdriver.Chrome()

# 啟動 CSV 檔案並寫入標題列
output_file = open('vip_vendors.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(output_file)
csv_writer.writerow(['公司名稱', '網址', '標籤資訊', '品牌名稱', '主要產品', '攤位號碼'])

while True:
    # 產生網址並開啟頁面
    computex_url = f'https://www.computextaipei.com.tw/zh-tw/exhibitor/show-area-data/index.html?pageSize={page_size}&currentPage={current_page}'
    driver.get(computex_url)

    # 找出所有 VIP 攤商
    vip_venders = driver.find_elements(By.CLASS_NAME, 'vip')

    if len(vip_venders) == 0:
        print("本頁無VIP攤商，視為結束爬蟲")
        break

    print(f"第 {current_page} 頁，共有 VIP 攤商數：{len(vip_venders)}")

    for vender in vip_venders:
        try:
            vender_name = vender.find_element(By.TAG_NAME, 'h3').text.strip()
            vender_url = vender.find_element(
                By.XPATH, './/h3/a').get_attribute('href')
            tags = [tag.text.strip()
                    for tag in vender.find_elements(By.XPATH, './/ul/li/a')]
            spans = vender.find_elements(By.XPATH, './/ul/li/span')
            ps = vender.find_elements(By.XPATH, './/ul/li/p')

            # 預設資訊欄位
            brand_name = ''
            main_product = ''
            booth = ''

            # 根據 span 的標題填入對應欄位
            for span, p in zip(spans, ps):
                key = span.text.strip().replace('：', '')
                value = p.text.strip()
                if key == '品牌名稱':
                    brand_name = value
                elif key == '主要產品':
                    main_product = value
                elif key == '攤位號碼':
                    booth = value

            # 寫入資料列
            csv_writer.writerow([vender_name, vender_url, ', '.join(
                tags), brand_name, main_product, booth])

            # Console 印出（可選）
            print(vender_name, vender_url, brand_name,
                  main_product, booth, tags)
            print()

        except Exception as e:
            print(f"錯誤發生：{e}")

    current_page += 1
    time.sleep(1)

driver.quit()
output_file.close()
print("已完成所有資料抓取與匯出！")
