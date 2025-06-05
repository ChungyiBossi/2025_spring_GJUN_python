from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

computex_url = 'https://www.computextaipei.com.tw/zh-tw/exhibitor/show-area-data/index.html'
computex_url += '?pageSize=100'
driver.get(computex_url)


# 選頁數
select_page_size = driver.find_element(By.ID, 'pageSize')
Select(select_page_size).select_by_value("40")
# 按下確定
check = driver.find_element(By.XPATH, '//input[@value="確定"]')
check.click()
while True:
    vip_venders = driver.find_elements(By.CLASS_NAME, 'vip')
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

    # 按下一頁
    try:
        nextpage = driver.find_element(By.XPATH, '//a[@aria-label="下一頁"]')
        nextpage.click()
    except Exception as e:
        break

    driver.implicitly_wait(1)  # 等待頁面加載
driver.quit()
