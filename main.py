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
######################################
## darknet updating by search terms on the onions sites website with graph and charts updating monthly etc.
## if its more than 1 of the same type of address don't add any of them
# more comphreensive onion sites to scrap from...
# have i2p verison? Add more coins, fix litecoin address etc
# check what my default headers say as tor, update it to the classical tor header
# make sure, to check every link against the duplicate list/ already been
# scrap all onion shit ton, and remove dups by onion address
urllib3.disable_warnings()
res = requests.get("http://www.ifconfig.me/ip", timeout=30)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.get_text())
header = {"header": "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"}

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo
# non-dup 2624 total onion sites scraped
website1 = ['http://torlinkv7cft5zhegrokjrxj2st4hcimgidaxdmcmdpcrnwfxrr2zxqd.onion/', 'http://fvrifdnu75abxcoegldwea6ke7tnb3fxwupedavf5m3yg3y2xqyvi5qd.onion/', 'http://4dtwo7g4yjqtiu7sta7icchm3f2aomvfv62xrgn6jc42lm43ut4aydqd.onion/', 'http://godnotawwdd5ttzwnfsfe7p5iimukt4p6mdxrlvzjv6v7nlqdihzygyd.onion/', 'http://gtl3bpvdnzijqmna2sd25ktixabzt7pval6fpkd2ur6vpov52zzv74yd.onion/', 'http://gtl3bpvdnzijqmna2sd25ktixabzt7pval6fpkd2ur6vpov52zzv74yd.onion/', 'http://wiki2zkamfya6mnyvk4aom4yjyi2kwsz7et3e4wnikcrypqv63rsskid.onion/', 'http://tordoge35c5krfwoghekqpe6zlbdgfafn5byppmgnthktzmtk4rjahqd.onion/', 'http://duckwm3krjkdpb7wbkgbra5bu7ilwr2wj5zjp6pym7clfprumwdluhid.onion/', 'http://4eoz4pemry55ioyns744kdvrqgmterzy5xlrairziuuxrjbmdipcyyad.onion/Recommend&Trust', 'http://trulv5o5ovg3hajltyr2wypzqrrtnkhcg4trstghtebvnrmxwmytdrad.onion/', 'http://4fkus6677knjgarqp2r7rhnpqdxzw7en7earran2djd7pye3nab2odqd.onion/', 'http://gtl3bpvdnzijqmna2sd25ktixabzt7pval6fpkd2ur6vpov52zzv74yd.onion/', 'http://torwin5lcn2um3brjftk7mm5gqeqtkocgevezejz6xxqyyk7xmcqndid.onion/index.php/Main_Page', 'http://wiki6dtqpuvwtc5hopuj33eeavwa6sik7sy57cor35chkx5nrbmmolqd.onion/', 'http://catalogxlotjjnu6vyevngf675vu6beefzxw6gd6a3fwgmgznksrqmqd.onion/', 'http://4dtwo7g4yjqtiu7sta7icchm3f2aomvfv62xrgn6jc42lm43ut4aydqd.onion/', 'http://olinkspc6xf2poogjgufztrly7rg347n2stmurhuqb7bjqgevsnyygid.onion/', 'http://dqbse3hopxlxpyoqwbm4v7cl43cplj44dajy2xinpaue4eaxmuclnhqd.onion/', 'http://wjsxwymbrjl7mmu3lj7xfqctpbfujtaieyjcixlnwnr57oad3yhfhxid.onion/', 'http://zaejy2lskzkbxo5vlc3qxs4mpwg25lgoadwtwxquvhkkq5eid43oqryd.onion/', 'http://hbwikiwsue3y74k6jyijzfdvc5h3lcgre3zwbjvghm4qngoj5wtuoeid.onion/', 'http://wikihqszbl62mzxncahyuyavw5n4ssfnpucemqnlu33akrkuwulflnyd.onion/', 'http://p23gulsmmneshdxabrbt3j2enmf2h4suynuujimjqjlklo4pprx6flid.onion/']
website2 = ["https://github.com/mounibkamhaz/DarkWeb", "https://github.com/darknet11/onionlink", "https://dark.fail/", 'http://torlinkv7cft5zhegrokjrxj2st4hcimgidaxdmcmdpcrnwfxrr2zxqd.onion/', 'http://wvqwxc2pv54vodexdspx45nto5brtuomdibcdc5xk22kjnjjseov6kid.onion/', 'http://nf2nip7s2235bzv4zw2vpndctw2bkz6qgzut6n7wx62sud5m27o5fwad.onion/']
website = ['https://github.com/mounibkamhaz/DarkWeb', 'https://lukesmith.xyz/', 'https://cakewallet.com/', 'https://www.erowid.org/donations/donations_cryptocurrency.php']
dataCollected = []
noWorkingData = []
cryptoList = []
workingOnionSite = []
addressCollected = []
keyTerms = [{'coin': r'bitcoin', 'ticker': r'btc[\-_:),. ]|[\b]'}, {'coin': r'monero', 'ticker': r'xmr[\-_:),. ]|[\b]'}, {'coin': r'ethereum', 'ticker': r'[\b]|eth[\-_:),. ]|[\b]'},  {'coin': r'zcash', 'ticker': r'zec[\-_:),. ]|[\b]'}, {'coin': r'tether', 'ticker': r'usdt[\-_:),. ]|[\b]'}, {'coin': r'litecoin', 'ticker': r'ltc[\-_:),. ]|[\b]'}]
regexList = [{'type': 'bitcoin', 'subtype': 'Bech32', 'regexAddress': r'bc1q[ac-hj-np-z02-9]{38}'},{'type': 'bitcoin', 'subtype': 'P2SH', 'regexAddress': r'\b3[a-km-zA-HJ-NP-Z1-9]{25,34}\b'}, {'type': 'bitcoin', 'subtype': r'P2PKH', 'regexAddress': r'1[A-Z][a-zA-HJ-NP-Z0-9]{32}\b'}, {'type': 'monero', 'subtype': 'main', 'regexAddress': r'4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}'}, {'type': 'monero', 'subtype': 'subaddress', 'regexAddress': r'8[0-9AB][1-9A-HJ-NP-Za-km-z]{93}'}, {'type': 'ethereum', 'subtype': None, 'regexAddress': r'0x[a-fA-F0-9]{40}'},
             {'type': 'litecoin', 'subtype': r'legacy', 'regexAddress': r'\bL[a-km-zA-HJ-NP-Z1-9]{33}\b'}, {'type': 'litecoin', 'subtype': r'native segwit', 'regexAddress': r'ltc[a-z0-9]{60}\b'}, {'type': 'litecoin', 'subtype': r'segwit', 'regexAddress': r'M[a-km-zA-HJ-NP-Z1-9]{33}\b'}, {'type': 'zcash', 'subtype': r'transparent', 'regexAddress': r't1[a-km-zA-HJ-NP-Z1-9]{33}'}, {'type': 'zcash', 'subtype': r'shielded', 'regexAddress': r'z1[a-km-zA-HJ-NP-Z1-9]{33}'}]
# add \b to front of legacy litecoin wallet
res = requests.get("http://www.ifconfig.me/ip", timeout=30)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.get_text())

# data = read_csv("onionSitesTorlink.csv")
# website1 = data['sites'].tolist()
#Excel, Power BI, SQL, Python
#scrapy? i2p scarper + graphs, regex all key words? crawl within site?? look for "donate" amd crawl that first..? somehow scrap dread once it up..? add website with dread/general onion sets ranked
#add more top coins like doge etc
#1499, (3954, 2485) (4261, 2578)
print(len(website1))
for enum, web in  enumerate(website1[0:1]):
    print(f' #: {enum}')
    try:
        res = requests.get(web, timeout=60, verify=False, headers=header)
        soup = BeautifulSoup(res.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            if a['href'].find('.onion') != -1:
                if a['href'].find('porn') == -1 and a['href'].find('?link=') == -1 and a['href'].find('teen') == -1 and a['href'].find('xxx') == -1 and a['href'].find('boy') == -1 and a['href'][0:2].find('cp') == -1:
                    dataCollected.append(a['href'])

    except Exception as e:
        print(f'Error: {web} {e}')

print(len(dataCollected))
dataCollected = list(set(dataCollected))
print(len(dataCollected))
# dataCollected = dataCollected[0:(round(len(dataCollected)/2))]
# dataCollected = dataCollected[(round(len(dataCollected)/2)):(round(len(dataCollected)))]
def regexSeacher(soup, site):
    txt = re.sub(r"[\n]*", "", soup.get_text()) # removed \t
    # txt = re.sub(r"[\n\t]*", "", soup.get_text()) # removed \t
    # print(txt)

    for regex in regexList:
        matched_address = re.findall(regex['regexAddress'], txt)
        if (len(matched_address) == 1) or (regex['type'] == 'ethereum' and len(matched_address) != 0 and len(matched_address) <= 4): #new code make sure only accept 1 of each address per website
            for address in matched_address:
                if len(address) <= 120:
                    print(address)
                    addressCollected.append(
                        {'address': address, 'website': site, 'type': regex['type'], 'subtype': regex['subtype']})

    for searchTerm in keyTerms:
        shortCoinList = re.findall(searchTerm['coin'], txt.lower())
        shortTickerList = re.findall(searchTerm['ticker'], txt.lower())
        if len(shortCoinList) != 0 or len(shortTickerList) != 0:
            cryptoList.append({'coin': searchTerm['coin'], 'count': (len(shortCoinList) + len(shortTickerList)), 'URL': site})



for enum, site in enumerate(dataCollected):
    try:
        print(enum, site, res.status_code)
        if enum % 1000 == 0 and enum != 0:
            print('Sleeping every 1000 scrapes')
            sleep(60*60*2)

        res = requests.get(site, timeout=random.randrange(20, 30), verify=False, headers=header) # I changed this to false

        if res.status_code == 200:
            workingOnionSite.append(site)
            soup = BeautifulSoup(res.content, 'html.parser')
            ahefList = []
            for a in soup.find_all('a', href=True):
                if a['href'].find('.onion') != -1 and a.get_text().lower().find('donate') != -1:
                    ahefList.append(a['href'])
                    print('Found donate!: ', a)

            ahefList = list(set(ahefList)) # turn verify = True, and compare it

            if len(ahefList) != 0:
                for x in ahefList:
                    res1 = requests.get(x, timeout=random.randrange(20, 30), verify=False, headers=header)
                    soup1 = BeautifulSoup(res1.content, 'html.parser')
                    regexSeacher(soup1, x)

            regexSeacher(soup, site)


            print("Key Term List: ",len(cryptoList), "# Addresses: ", len(addressCollected))
        else:
            print('Website Status Failure: ', res.status_code)

    except Exception as e:
        print(f'Error: {res.status_code, e}')

print(len(workingOnionSite))
print('Before dup')
print(len(cryptoList))
print(len(addressCollected))

addressCollected = [i for n, i in enumerate(addressCollected) if i not in addressCollected[n + 1:]]
cryptoList = [i for n, i in enumerate(cryptoList) if i not in cryptoList[n + 1:]]

print('After dup')
print(len(cryptoList))
print(len(addressCollected))

df = pd.DataFrame(data={"sites": workingOnionSite})
df.to_csv("onionSiteTesting1.csv", sep=',',index=False, encoding='UTF8')

with open('coinDataTesting1.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.DictWriter(f, fieldnames=['coin', 'URL', 'count'])
    writer.writeheader()
    writer.writerows(cryptoList)

with open('onionAddressesTesting1.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.DictWriter(f, fieldnames=['address', 'website', 'type', 'subtype'])
    writer.writeheader()
    writer.writerows(addressCollected)

for x in cryptoList:
    print(x)

for x in addressCollected:
    print(x['address'], x['type'], x['subtype'])