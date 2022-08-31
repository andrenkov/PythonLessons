# In the File --> Settings --> Project --> interpreter add: Requests
# request lib : requests
# parsing lib : BS4

import requests, bs4

# GET
# url = "https://market.yandex.ru/catalog--mobilnye-telefony/34512430/list?hid=91491&local-offers-first=1"
# url = url = "https://cacticorner.ca/cartsearch/index.html?rootCategory=aoywduvn"
url ="http://avlad.no-ip.info:9091/Seeds/CatalogPages"
req = requests.get(url)
# req.encoding = 'UTF8'
# print(req.text)

#Parsing by html tag <a> and class <n-snippet-cell2__title>
bs = bs4.BeautifulSoup(req.text, "html.parser")
# atitles = bs.select("div.n-snippet-cell2__title a")  # select all elements "a" inside tag div of class "n-snippet-cell2__title"
# atitles = bs.select("div.im-products-name")
# atitles = bs.select("td a")
atitles = bs.select("table td")

aData = []
for a in atitles:  # array of objects
    if a.getText():
        # print(a.getText())
        # atitles.append(a)
        aData.append(a.getText())

print(aData)



