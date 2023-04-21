import socks
import socket
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import re
import datetime
from fake_user_agent import user_agent
import random
import urllib3
import sys
from pandas import *

import urllib3

newDict = []
urllib3.disable_warnings()
headers = {'User-Agent': user_agent()}
date = str(datetime.datetime.now())
month = datetime.datetime.now()
#'month': month.strftime("%B")
# df2 = pd.read_csv('onionAddressesFeb.csv', encoding='UTF8')
# df3 = pd.read_csv('onionAddre ssesFeb2.csv', encoding='UTF8')
# frames = [df2, df3]
# df = pd.concat(frames)
# df = df.drop_duplicates(subset=['address'])
# df.to_csv('onionAddressesFebTotal.csv', encoding='UTF8')

reader = csv.DictReader(open('onionAddresses2023-03-31.csv'))
for enum, row in enumerate(reader):
    try:
        res = requests.get(f"https://blockchair.com/{row['type']}/address/{row['address']}", timeout=30, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        span1 = soup.findAll('span', {'class': 'account-hash__balance__values'})[0]
        span2 = soup.findAll('span', {'class': 'account-hash__balance__values'})[1]
        currentBalance = span1.findAll('span', {'class': 'wb-ba'})[0]
        totalReceived = span2.findAll('span', {'class': 'wb-ba'})[0]
        print(enum,currentBalance.get_text().replace(",", ""), "-", totalReceived.get_text().replace(",", ""), row['address'])

        newDict.append(
            {'currentBalance': float(currentBalance.get_text().replace(",", "")), 'totalReceived': float(totalReceived.get_text().replace(",", "")), 'type': row['type'], 'address': row['address'], 'website': row['website'],
             'subtype': row['subtype'], 'month': month.strftime("%B")})
    except Exception as e:
        print(enum, "NaN", "NaN", row['type'])

        newDict.append(
            {'currentBalance': "NaN", 'totalReceived': "NaN",
             'type': row['type'], 'address': row['address'], 'website': row['website'],
             'subtype': row['subtype'], 'month': month.strftime("%B")})


print("-----------------------")
for x in newDict:
    print(x)

with open(f'onionAddressesBalance{date[0:10]}.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.DictWriter(f, fieldnames=['address', 'website', 'type', 'subtype', 'currentBalance', 'totalReceived'])
    writer.writeheader()
    writer.writerows(newDict)










