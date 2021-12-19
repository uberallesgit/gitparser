import requests
from bs4 import BeautifulSoup
import lxml
import json


# headers = {
#     "Accept": "*/*",
# "User-Agent" :"Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
# }
url = "http://mebel-saa.ru"
#
# req = requests.get(url,headers=headers)
# src = req.text
# print(src)
# with open("index.html","w") as file:
#     file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src,"lxml")

all_hrefs = soup.find_all("a")

all_product_hrefs = []

# for item in all_hrefs:
    # print(count,item.text)

all_product_hrefs = all_hrefs[5:43]
all_products_links = []
all_product_images = []
count = 0

all_categories_dict = {}

for item in all_product_hrefs:
    item_text = item.text
    item_href = item.get("href")

    all_categories_dict[item_text] = item_href
    count+=1
    print(f"{count}-{item_text} {url + item_href}")










