import requests
from bs4 import BeautifulSoup
import lxml
import json
import csv


headers = {
    "Accept": "*/*",
"User-Agent" :"Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
}
url = "http://mebel-saa.ru"
# #
# req = requests.get(url,headers=headers)
# src = req.text
# print(src)
# with open("index.html","w") as file:
#     file.write(src)

# with open("index.html") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src,"lxml")
#
# all_hrefs = soup.find_all("a")
#
# all_product_hrefs = []
#
# # for item in all_hrefs:
#     # print(count,item.text)
#
# all_product_hrefs = all_hrefs[5:22]
# all_products_links = []
# all_product_images = []
#
#
# count = 0
#
# all_categories_dict = {}
#
# for item in all_product_hrefs:
#     print(count,item)
#     item_text = item.text
#     item_href = item.get("href")
#
#     all_categories_dict[item_text] = url+item_href
#     count += 1
#
#     #Создаём json файл
#
#
# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_categories_dict.json") as file:
    all_categories = json.load(file)

count = 0
for category_name,category_href in all_categories.items():

    rep = [","," ","-"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    req = requests.get(url=category_href,headers=headers)
    src = req.text
    with open(f"data/{category_name}.html", "w") as file:
        file.write(src)

    with open(f"data/{category_name}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src,"lxml")

        #собираем заголвки таблицы
    head_name = "Наименование"
    head_href = "Ссылка"
    head_price = "Цена"



    names = soup.find_all("h2", class_="catItemTitle")
    names_count = 0

    # for name in names:
    #     print(names_count,name.text.strip())
    #     names_count+=1

    with open(f"data/{count}_{category_name}.csv","w",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                head_name,
                head_price,
                head_href

            )
        )

    # собираем данные продуктов
    furniture = soup.find_all("h2",class_="catItemTitle")
    prices = soup.find("div", id="itemListLeading").find_all("div", class_="catItemPrice")
    prices_count = 0
    for item in prices:
        prices_count+=1
        # print(prices_count)

    links = soup.find("div", id="itemListLeading").find_all("a")
    # print(links)
    fur_list = []
    price_list = []
    link_list = []
    county = 0
    while county < prices_count:
        for item in furniture:
            # print(item.text.strip())
            fur_list.append(item.text.strip())

        for price in prices:
            #
            price = price.text
            price_list.append(price)



        link_count = 0
        for link in links:
            link = url+link.get("href")
            if link_count % 3 == 0:
                link_list.append(link)
            link_count +=1




        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8")as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    fur_list[county],
                    price_list[county],
                    link_list[county]
                )
            )

        county += 1
    # print(link_list)



    # print(link_list)





    count += 1

print(f"Парсинг сайта окончен! Вся необходимая информация находится в папке data")

























