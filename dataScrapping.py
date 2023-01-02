import socks
import socket
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import re
from fake_user_agent import user_agent


#'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1'

headers = {'User-Agent': user_agent()}

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
## darknet updating by search terms on the onions sites website with graph and charts updating monthly etc.
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

website1 = ["http://torlinkv7cft5zhegrokjrxj2st4hcimgidaxdmcmdpcrnwfxrr2zxqd.onion/"]
website2 = ["https://github.com/mounibkamhaz/DarkWeb", "https://github.com/darknet11/onionlink", "https://dark.fail/", 'http://torlinkv7cft5zhegrokjrxj2st4hcimgidaxdmcmdpcrnwfxrr2zxqd.onion/', 'http://wvqwxc2pv54vodexdspx45nto5brtuomdibcdc5xk22kjnjjseov6kid.onion/', 'http://nf2nip7s2235bzv4zw2vpndctw2bkz6qgzut6n7wx62sud5m27o5fwad.onion/']
website = ['https://github.com/mounibkamhaz/DarkWeb', 'https://lukesmith.xyz/', 'https://cakewallet.com/', 'https://www.erowid.org/donations/donations_cryptocurrency.php']
dataCollected = []
noWorkingData = []
cryptoList = []
addressCollected = []
keySearchTerms = [r'bitcoin', r'monero', r'litecoin', r'zcash', r'ethereum', r'tether']
keySearchTickers = [ r'\bbtc\b', r'\bxmr\b', r'\beth\b', r'\bltc\b', r'\bzec\b', r'\bUSDT\b']
keyTerms = [{'coin': r'bitcoin', 'ticker': r'\bbtc\b'}, {'coin': r'monero', 'ticker': r'\bxmr\b'}, {'coin': r'ethereum', 'ticker': r'\beth\b'},  {'coin': r'zcash', 'ticker': r'\bzec\b'}, {'coin': r'tether', 'ticker': r'\USDT\b'}]


regexList = [{'type': 'bitcoin', 'subtype': 'native segwit', 'regexAddress': r'bc1q[ac-hj-np-z02-9]{38}'},{'type': 'bitcoin', 'subtype': 'P2SH', 'regexAddress': r'\b3[a-km-zA-HJ-NP-Z1-9]{25,34}\b'}, {'type': 'bitcoin', 'subtype': r'legacy', 'regexAddress': r'[1][A-Z][a-zA-HJ-NP-Z0-9]{32}\b'}, {'type': 'monero', 'subtype': 'main', 'regexAddress': r'[4][0-9AB][1-9A-HJ-NP-Za-km-z]{93}'}, {'type': 'monero', 'subtype': 'subaddress' , 'regexAddress': r'[8][0-9AB][1-9A-HJ-NP-Za-km-z]{93}'}, {'type': 'ethereum', 'subtype': None, 'regexAddress': r'0x[a-fA-F0-9]{40}'}, {'type': 'litecoin', 'subtype': r'legacy', 'regexAddress': r'[L][a-km-zA-HJ-NP-Z1-9]{33}\b'}, {'type': 'litecoin', 'subtype': r'segwit', 'regexAddress': r'[M][a-km-zA-HJ-NP-Z1-9]{33}\b'}, {'type': 'zcash', 'subtype': r'transparent', 'regexAddress': r't1[a-km-zA-HJ-NP-Z1-9]{33}'}, {'type': 'zcash', 'subtype': r'shielded', 'regexAddress': r'z1[a-km-zA-HJ-NP-Z1-9]{33}'}]
workingOnionSite = []
# eth regex add : and \b
#scrapy? regex all key words? crawl within site?? look for "donate" amd crawl that first..? somehow scrap dread once it up..? add website with dread/general onion sets ranked
#bc1q[ac-hj-np-z02-9]{38}
#bc(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})|1[ac-hj-np-z02-9]{8,87})

for web in website:
    try:
        res = requests.get(web, timeout=30, headers=headers, verify=True)
        print("Header: ", res.request.headers, res.status_code)
        soup = BeautifulSoup(res.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            if a['href'].find('.onion') != -1:
                if a['href'].find('porn') == -1 and a['href'].find('teen') == -1 and a['href'].find('xxx') == -1 and a['href'].find('boy') == -1 and a['href'][0:2].find('cp') == -1:
                    dataCollected.append(a['href'])

    except Exception as e:
        print(f'Error: {e}')

print(len(dataCollected))
dataCollected = list(set(dataCollected))
print(len(dataCollected))
dataCollected = dataCollected[882:1329] ##882:1329
print(len(dataCollected))
print(dataCollected)

for enum, site in enumerate(website):
    sleep(15)
    print(enum, site)
    try:
        res = requests.get(site, timeout=30, verify=True, headers=headers)
        if res.status_code == 200:
            workingOnionSite.append(site)
            soup = BeautifulSoup(res.content, 'html.parser')
            txt = re.sub(r"[\n\t]*", "", soup.get_text())

            for regex in regexList:
                matched_address = re.findall(regex['regexAddress'], txt)
                for address in matched_address:
                    if len(address) <= 150:
                       addressCollected.append({'address': address, 'website': site, 'type': regex['type'], 'subtype': regex['subtype']})

            for searchTerm in keyTerms:
                shortCoinList = re.findall(searchTerm['coin'], txt.lower())
                shortTickerList = re.findall(searchTerm['ticker'], txt.lower())

                if len(shortCoinList) != 0 or len(shortTickerList) != 0:
                    cryptoList.append({'coin': searchTerm['coin'], 'count': len(shortCoinList) + len(shortTickerList), 'URL': site})


            print(len(cryptoList), len(addressCollected))

    except Exception as e:
        print(f'Error: {e}')


print(len(workingOnionSite))


df = pd.DataFrame(data={"sites": workingOnionSite})
df.to_csv("onionSitesTest.csv", sep=',',index=False)

with open('coinDataTest.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['coin', 'URL', 'count'])
    writer.writeheader()
    writer.writerows(cryptoList)

with open('onionAddressesTest.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['address', 'website', 'type', 'subtype'])
    writer.writeheader()
    writer.writerows(addressCollected)


for x in cryptoList:
    print(x)


print(addressCollected)

for x in addressCollected:
    print(x['address'], x['type'], x['subtype'])

