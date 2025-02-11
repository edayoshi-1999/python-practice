from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from bs4 import BeautifulSoup


driver = webdriver.Chrome()
url_test = "https://tonari-it.com/omikuji"
# url = "https://tonari-it.com"
driver.maximize_window()
driver.get(url_test)

# print(driver.name)
# print(driver.title)
# print(driver.current_url)
# soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup.title)

# print(driver.find_element(By.ID, "hoge").text)

# def print_elements(elements):
#     for element in elements:
#         print(element.text)
# print_elements(driver.find_elements(By.TAG_NAME, "h2"))

# ths = driver.find_element(By.TAG_NAME, "thead")\
#             .find_element(By.TAG_NAME, "tr")\
#             .find_elements(By.TAG_NAME, "th")
# print(ths[0].text, ths[1].text)
# driver.quit()

# try:
#     button = driver.find_element(By.ID, "nonexist")
# except NoSuchElementException as e:
#     print("要素がなかった", e)
# else:
#     button.click()
# finally:
#     driver.quit()

# button = driver.find_element(By.ID, "omikuji")
# print("click前")
# button.click()
# print("clikc後")

# textbox = driver.find_element(By.NAME, "s")
# textbox.send_keys("python", "初心者")
# textbox.submit()

driver.quit()