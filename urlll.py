import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

url_3 = 'https://search.codal.ir/api/search/v2/q?&Audited=true&AuditorRef=-1&Category=1&Childs=true&CompanyState=-1&CompanyType=-1&Consolidatable=true&IsNotAudited=false&Length=-1&LetterType=6&Mains=true&NotAudited=true&NotConsolidatable=true&PageNumber=1&Publisher=false&TracingNo=-1&search=true'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
response_3 = requests.get(url=url_3, headers=header)
aaa = response_3.text.split('SuperVision":{')[1:]
data = []
tickers = []
names = []
# print(len(aaa))

for a in aaa[:]:
    # print(a)
    ticker = a.split('Symbol":"')[1].split('"')[0]
    name = a.split('CompanyName":"')[1].split('"')[0]
    print(ticker, name)
    tickers.append(ticker)
    names.append(name)

    # a = a.split(',')
    # for b in a:
    #     print(b)

# product = {'Ticker': tickers, 'Name': names}
# print(product)
