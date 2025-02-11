import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://tonari-it.com/scraping-test/"
# params = {"s": "python"}
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")
# print(soup.find("title"))
# print(soup.find("h2"))
# print(soup.find(attrs={"id": "hoge"}))
# print(soup.find_all("h2", limit=2))
# print(soup.find_all(attrs={"class": "fuga"}))
# print(soup.select("h2"))
# print(soup.select("#hoge"))
# print(soup.select(".fuga"))
# print(soup.select("#post-32150 > div > p:nth-child(5)"))

# tag = soup.find(attrs={"id": "hoge"})
# print(tag)
# print(tag.name)
# print(tag.attrs)
# print(tag.text)
# ths = soup.find("thead").find("tr").find_all("th")
# print(ths)

# soup = BeautifulSoup(r.text, "html.parser")
# [tag.extract() for tag in soup.find_all(string="\n")]
# tr = soup.find("tr")
# print(tr.parent.name)
# print(tr.contents)
# for child in tr.children:
#     print(child)
# tr.clear()
# print(tr)

dfs = pd.read_html(url)
print(dfs[0])