from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome()
url = "https://tonari-it.com/omikuji/"
driver.get(url)

button = driver.find_element(By.ID, "omikuji")
button.click()
msg = driver.find_element(By.ID, "msg")

data = {
    "日付": [datetime.now()],
    "おみくじ結果": [msg.text]
}

df = pd.DataFrame(data)
# print(df)
df.to_csv(r"chapter11\omikuji.csv", header=False, index=False, mode="a")

driver.quit()