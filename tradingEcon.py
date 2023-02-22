import socks
import socket
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import re
from fake_user_agent import user_agent
import random
import urllib3
import sys
from pandas import *
from stem import Signal
from stem.control import Controller
import urllib3
# urllib3.disable_warnings()
# headers = {'User-Agent': user_agent()}
# print(headers)
# res = requests.get("https://tradingeconomics.com/country-list/government-debt-to-gdp", timeout=30, headers=headers)
# soup = BeautifulSoup(res.content, 'html.parser')
# # print(soup.prettify())
# data = soup.find_all("tr", {"class": "datatable-row"})
# data2 = soup.find_all("tr", {"class": "datatable-row-alternating"})
# debtToGDP = []
# # //*[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]/div/div/table/tbody
# # class="datatable-row"
#
# for row in data:
#     debtToGDP.append({'debtToGDP': float(row.find_all("td")[1].get_text()), 'country': row.find_all("td")[0].get_text().strip()})
#     print("--------------")
#
# for row in data2:
#     debtToGDP.append(
#         {'debtToGDP': float(row.find_all("td")[1].get_text()), 'country': row.find_all("td")[0].get_text().strip()})
#     print("--------------")
#
# # for row in data2:
# #     print(row.find_all("td")[0].get_text().strip())
# #     debtToGDP.append(row.find_all("td")[1].get_text().strip())
# #     # print("--------------")
#
#
# # print(debtToGDP)
# df = pd.DataFrame(debtToGDP)
# df = df.sort_values(by=['debtToGDP'], ascending=False)
# df = df.reset_index()
# print(df[['country', 'debtToGDP']][0:50])
# df.to_csv(debtToGDP.csv, sep='\t', encoding='utf-8')
# from tkinter import Tk  # Python 3
# #from Tkinter import Tk # for Python 2.x
# data = Tk().clipboard_get()
# print(data)
import datetime

date = str(datetime.datetime.now())

print(date[0:10])
