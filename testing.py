from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import FirefoxOptions

#C:\Users\Monies\Tor Browser\Browser\firefox.exe
#C:\Users\Monies\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default"
from selenium import webdriver
import selenium
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

print(selenium.__version__)
options = Options()
options.binary_location = r'C:\Users\Monies\Tor Browser\Browser\firefox.exe'
options.set_preference('profile', r'C:\Users\Monies\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9010)
options.set_preference('network.proxy.socks_remote_dns', False)
# options.set_preference("browser.download.folderList",2)
# options.set_preference("browser.download.manager.showWhenStarting", False)
# options.set_preference("browser.download.dir","/Data")
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

# service = Service(r'C:\Users\Monies\Downloads\gecko1\geckodriver.exe')
browser = webdriver.Firefox(options=options)
# binary = FirefoxBinary(r'C:\Users\Monies\Downloads\geckodriver.exe')
# browser = webdriver.Firefox(options=options, firefox_binary=binary)
# driver = webdriver.Firefox(options=options)
# browser.get("https://httpbin.org/ip")
# time.sleep(5)
# browser.quit()
