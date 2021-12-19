import requests
from bs4 import BeautifulSoup
import lxml


# headers = {
#     "Accept": "*/*",
# "User-Agent" :"Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
# }
# url = "http://mebel-saa.ru/"
#
# req = requests.get(url,headers=headers)
# src = req.text
# print(src)
# with open("index.html","w") as file:
#     file.write(src)

with open("index.html") as files:
    src = file.read()




