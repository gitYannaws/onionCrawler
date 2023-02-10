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
urllib3.disable_warnings()
headers = {'User-Agent': user_agent()}
print(headers)
res = requests.get("https://tradingeconomics.com/country-list/government-debt-to-gdp", timeout=30, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())
data = soup.find_all("tr", {"class": "datatable-row"})
# //*[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]/div/div/table/tbody
# class="datatable-row"
for row in data:
    print(row.find_all("td")[1].get_text())
    print("--------------")