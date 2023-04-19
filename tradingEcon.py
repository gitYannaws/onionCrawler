import socks
import socket
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import re
import random
import urllib3
import sys
from pandas import *

import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
