import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://tonari-it.com"
query = "Python 初心者"
params = {"s": query}
r = requests.get(url, params=params)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
h2s = soup.find_all("h2")
anchors = soup.find_all("a", attrs={"class": "entry-card-wrap a-wrap border-element cf"})

# for h2, anchor in zip(h2s, anchors):
#     print(h2.text, anchor.attrs["href"])

values = []
for h2, anchor in zip(h2s, anchors):
    values.append([h2.text, anchor.attrs["href"]])

filename = rf"chapter10/tonari-it_{query}.xlsx"
df = pd.DataFrame(values, columns=["タイトル", "URL"])
df.index = df.index +1
df.to_excel(filename)