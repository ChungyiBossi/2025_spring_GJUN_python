from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# webdriver.Firefox()
# webdriver.Safari()
# webdriver.Edge()
driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

print("Title: ", driver.title)

# driver.implicitly_wait(10)
text_box = driver.find_element(By.NAME, "my-text")
submit_button = driver.find_element(By.TAG_NAME, "button")
radio_default = driver.find_element(
    By.XPATH, '//label/input[@id="my-radio-2"]')
# radio_default.click()
print("Default Radio: ", radio_default.is_selected())

time.sleep(3)  # 等他一下
text_box.send_keys("Selenium")
submit_button.click()
time.sleep(3)  # 等他一下

message = driver.find_element(by=By.ID, value="message")
text = message.text
print('Text: ', text)
time.sleep(10)
driver.quit()
