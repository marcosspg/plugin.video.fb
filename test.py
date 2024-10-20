import os
from selenium import webdriver



# torexe = os.popen('C://Users//mapeg//OneDrive//Documents//Tor_Browser//Browser//firefox.exe')
# PROXY = "socks5://localhost:9050"
# options = webdriver.ChromeOptions()
# options.add_argument(f'--proxy-server={PROXY}')
# driver = webdriver.Chrome(chrome_options=options)

# driver.get("https://elcano.top")

# input("a")


from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

torPath = "C:/Users/mapeg/OneDrive/Documents/Tor_Browser"

binary = FirefoxBinary(f"{torPath}/Browser/firefox.exe")
profile = FirefoxProfile(f"{torPath}/Browser/TorBrowser/Data/Browser/profile.default")

driver = webdriver.Firefox(profile, binary)
driver.get("https://elcano.top")