import socks
import socket
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import re
import pandas as pd

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

website = ["https://github.com/mounibkamhaz/DarkWeb", "https://github.com/darknet11/onionlink", "https://dark.fail/", 'http://torlinkv7cft5zhegrokjrxj2st4hcimgidaxdmcmdpcrnwfxrr2zxqd.onion/', 'http://wvqwxc2pv54vodexdspx45nto5brtuomdibcdc5xk22kjnjjseov6kid.onion/']
test = ['http://ransomwr3tsydeii4q43vazm7wofla5ujdajquitomtd47cxjtfgwyyd.onion/','https://github.com/mounibkamhaz/DarkWeb', 'https://lukesmith.xyz/', 'freedom hosting','http://fhostingineiwjg6cppciac2bemu42nwsupvvisihnczinok362qfrqd.onion/', 'https://cakewallet.com/', 'https://www.erowid.org/donations/donations_cryptocurrency.php', 'http://darkfailenbsdla5mal2mxn2uz66od5vtzd5qozslagrfzachha3f3id.onion/', 'http://hbwikiwsue3y74k6jyijzfdvc5h3lcgre3zwbjvghm4qngoj5wtuoeid.onion/', 'http://olinkspc6xf2poogjgufztrly7rg347n2stmurhuqb7bjqgevsnyygid.onion/', 'http://p23gulsmmneshdxabrbt3j2enmf2h4suynuujimjqjlklo4pprx6flid.onion/', 'http://22tojepqmpah32fkeuurutki7o5bmb45uhmgzdg4l2tk34fkdafgt7id.onion/']
dataCollected = []
noWorkingData = []
cryptoList = []
addressCollected = []
keySearchTerms = [r'bitcoin', r'monero', r'litecoin', r'zcash', r'ethereum', r'tether', r'btc', r'xmr', r'\beth', r'ltc', r'\bzec']
regexList = [{'type': 'bitcoin', 'subtype': 'native segwit', 'regexAddress': r'bc1q[ac-hj-np-z02-9]{38}'},{'type': 'bitcoin', 'subtype': 'P2SH', 'regexAddress': r'\b3[a-km-zA-HJ-NP-Z1-9]{25,34}\b'}, {'type': 'bitcoin', 'subtype': r'legacy', 'regexAddress': r'[1][A-Z][a-zA-HJ-NP-Z0-9]{32}\b'}, {'type': 'monero', 'subtype': 'main', 'regexAddress': r'[4][0-9AB][1-9A-HJ-NP-Za-km-z]{93}'}, {'type': 'monero', 'subtype': 'subaddress' , 'regexAddress': r'[8][0-9AB][1-9A-HJ-NP-Za-km-z]{93}'}, {'type': 'ethereum', 'subtype': None, 'regexAddress': r'0x[a-fA-F0-9]{40}'}, {'type': 'litecoin', 'subtype': r'legacy', 'regexAddress': r'[L][a-km-zA-HJ-NP-Z1-9]{33}\b'}, {'type': 'litecoin', 'subtype': r'segwit', 'regexAddress': r'[M][a-km-zA-HJ-NP-Z1-9]{33}\b'}, {'type': 'zcash', 'subtype': r'transparent', 'regexAddress': r't1[a-km-zA-HJ-NP-Z1-9]{33}'}, {'type': 'zcash', 'subtype': r'shielded', 'regexAddress': r'z1[a-km-zA-HJ-NP-Z1-9]{33}'}]
workingOnionSite = []

#scrapy? regex all key words? crawl within site??
#bc1q[ac-hj-np-z02-9]{38}
#bc(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})|1[ac-hj-np-z02-9]{8,87})

for web in website:
    try:
        res = requests.get(web, timeout=15)
        soup = BeautifulSoup(res.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            if a['href'].find('.onion') != -1 and a['href'].find('porn') == -1 and a['href'].find('teen') == -1 and a['href'].find('xxx') == -1 and a['href'].find('boy') == -1 and a['href'][0:2].find('cp') == -1:
                dataCollected.append(a['href'])

    except Exception as e:
        print(f'Error: {e}')

print(len(dataCollected))
dataCollected = list(set(dataCollected))
print(len(dataCollected))


for enum, site in enumerate(dataCollected):
    sleep(1)
    print(enum, site)
    try:
        res = requests.get(site, timeout=30, verify=False)
        if res.status_code == 200:
            workingOnionSite.append(site)
            soup = BeautifulSoup(res.content, 'html.parser')
            txt = re.sub(r"[\n\t]*", "", soup.get_text())

            for regex in regexList:
                matched_address = re.findall(regex['regexAddress'], txt)
                for address in matched_address:
                    if len(address) <= 150:
                       addressCollected.append({'address': address, 'website': site, 'type': regex['type'], 'subtype': regex['subtype']})

            for searchTerm in keySearchTerms:
                shortCryptoList = re.findall(searchTerm, txt.lower())
                if len(shortCryptoList) != 0:
                    cryptoList.append({'coin': searchTerm, 'count': len(shortCryptoList), 'URL': site})


            print(len(cryptoList), len(addressCollected))

    except Exception as e:
        print(f'Error: {e}')


print(len(workingOnionSite))


df = pd.DataFrame(data={"sites": workingOnionSite})
df.to_csv("onionSites.csv", sep=',',index=False)



with open('coinData.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['coin', 'URL', 'count'])
    writer.writeheader()
    writer.writerows(cryptoList)

with open('onionAddresses.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['address', 'website', 'type', 'subtype'])
    writer.writeheader()
    writer.writerows(addressCollected)


for x in cryptoList:
    print(x)


print(addressCollected)

for x in addressCollected:
    print(x['address'], x['type'], x['subtype'])

