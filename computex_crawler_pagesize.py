from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

page_size = 500
current_page = 1
driver = webdriver.Chrome()

# 問題一：如何讓while結束 -> 假設每一頁都有vip，若找不到vip就跳出(那一頁沒有東西)
# 問題二：我要累加我的current_page，在當頁爬蟲結束後
# 問題三：把資料檔案匯出

while True:
    # 去拿每一頁的列表
    computex_url = 'https://www.computextaipei.com.tw/zh-tw/exhibitor/show-area-data/index.html'
    computex_url += f'?pageSize={page_size}&currentPage={current_page}'
    driver.get(computex_url)
    vip_venders = driver.find_elements(By.CLASS_NAME, 'vip')

    # 問題一的解決
    if len(vip_venders) == 0:
        print("本頁無VIP攤商，視為結束爬蟲")
        break

    print('# of VIP: ', len(vip_venders))
    for vender in vip_venders:
        vender_name = vender.find_element(By.TAG_NAME, 'h3')
        vender_url = vender.find_element(By.XPATH, './/h3/a')
        spans = vender.find_elements(By.XPATH, './/ul/li/span')
        ps = vender.find_elements(By.XPATH, './/ul/li/p')
        tags = vender.find_elements(By.XPATH, './/ul/li/a')

        print(vender_name.text)
        print(vender_url.get_attribute('href'))
        # print("<span>: ", [span.text for span in spans])
        # print("<p>: ", [p.text for p in ps])
        for key, value in zip(spans, ps):
            print(key.text, value.text)

        print("#tag: ", [tag.text for tag in tags])
        print()

    # 問題二的解決
    current_page += 1  # current_page = current_page + 1

    driver.implicitly_wait(1)  # 等待頁面加載
driver.quit()
