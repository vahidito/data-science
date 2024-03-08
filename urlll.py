import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
url = 'https://www.varzesh3.com/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.text)


url_3 = 'https://www.skysports.com/premier-league-table'
response_3 = requests.get(url_3)
soup_3 = bs(response_3.text, 'html.parser')
table_3 = soup_3.find('table')
rows = table_3.find_all('tr')
print(rows)
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