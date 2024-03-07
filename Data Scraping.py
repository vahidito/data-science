# Data Scraping

## Session_1
### Introduction

# _____________________________________________________________________________________________________________________

## Session_2
###_Install_Libraries

# in this session we installed the requests and Beautifulsoup packages

# _____________________________________________________________________________________________________________________

## Session_3
###_Exploring the requests package

import requests

url = "https://www.python.org/"
response = requests.get(url)

print(response.request.headers)
print(type(response.request.headers))
print(response.status_code)
print(response.reason)
print(response.headers)
print(response.text)  # source code
url_1 = "https://www.python.org/static/img/python-logo.png"
respo = requests.get(url_1)
with open("1.jpg", 'wb') as r:
    r.write(respo.content)

# _____________________________________________________________________________________________________________________

## Session_4
###_Exploring the BeautifulSoup package







# _____________________________________________________________________________________________________________________

