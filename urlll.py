import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
url = 'http://old.tsetmc.com/Loader.aspx?ParTree=15'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup.text)

# table_3 = soup_3.find('table')
# rows = table_3.find_all('tr')
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
