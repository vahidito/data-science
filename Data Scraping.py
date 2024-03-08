# Data Scraping

## Session_1
### Introduction

# _____________________________________________________________________________________________________________________

## Session_2
###_Install_Libraries

import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

# in this session we installed the requests and Beautifulsoup packages

# _____________________________________________________________________________________________________________________

## Session_3
###_Exploring the requests package
#

#
# url = "https://www.python.org/"
# response = requests.get(url)

# print(response.request.headers)
# print(type(response.request.headers))
# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.text)  # source code
# url_1 = "https://www.python.org/static/img/python-logo.png"
# respo = requests.get(url_1)
# with open("1.jpg", 'wb') as r:
#     r.write(respo.content)

# _____________________________________________________________________________________________________________________

## Session_4
###_Exploring the BeautifulSoup package

# soup = bs(response.text, 'html.parser')
# # print(soup)
# show = soup.find('a')
# show = soup.findAll('a')
# for s in show:
#     print(s['href'])

# show1 = soup.select_one('button.search-button')
# print(show1.text.strip())
# show2 = soup.find('button', {'id': 'submit'})
# print(show2.text.strip())
# print(show)

url_3 = 'https://www.skysports.com/premier-league-table'
response_3 = requests.get(url_3)
soup_3 = bs(response_3.text, 'html.parser')
table_3 = soup_3.find('table')
rows = table_3.find_all('tr')
# print(rows)
# for row in rows:
#     data = []
#     for head in row.findAll('th'):
#         # print(head.text)
#         heads = head.text
#         data.append(heads)
#
#     for body in row.findAll('td')[0:-1]:
#         bodies = body.text.replace('\n', '')
#         data.append(bodies)
#     print(data)

# _____________________________________________________________________________________________________________________
## Session_5
### Scraping data from digikala site

url_4 = 'https://www.digikala.com/search/category-mobile-phone/product-list/'
titles = []
stars = []
prices = []
page_4 = requests.get(url_4)
# print(page_4.text)
soup_4 = bs(page_4.text, 'html.parser')

title = soup_4.select(
    'div.ellipsis-2 text-body2-strong text-neutral-700 styles_VerticalProductCard__productTitle__6zjjN')
# print(title)
for t in title:
    name = t.text.strip()
    titles.append(name)

star = soup_4.select(
    'div.ellipsis-2 text-body2-strong text-neutral-700 styles_VerticalProductCard__productTitle__6zjjN')
# print(title)
for s in star:
    rate = s.text.strip()
    titles.append(rate)
price = star = soup_4.select(
    'div.ellipsis-2 text-body2-strong text-neutral-700 styles_VerticalProductCard__productTitle__6zjjN')
for p in price:
    pr = p.text.strip()
    prices.append(pr)

product = {'Title': titles, 'Star': stars, 'Price': prices}
data = pd.DataFrame.from_dict(product, orient='index')
data = data.transpose()
writer = pd.ExcelWriter('product.xlsx')
data.to_excel(writer)
writer.save()

# _____________________________________________________________________________________________________________________
