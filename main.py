from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

class bcolors:
    SUCCES = '\033[94m'
    ERROR = '\033[93m'

chrome_options = Options()
chrome_options.add_argument(
     '--user-agent=Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0. 3945.79 Mobile Safari/537.36')
browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)
url = "https://haveibeenpwned.com/unifiedsearch/"
fichier = open('email.txt', "r")
ligne = fichier.readlines()
fn = open("succes.txt", "w+")

for line in ligne:
    time.sleep(3)
    goodurl = url + line.strip()
    browser.get(goodurl)
    try:
        browser.find_element_by_id("main-frame-error")
        fn.write(line.strip()  + '\n')
        print(bcolors.SUCCES + "| WakerChecker | " + line.strip() + " is not public !")
    except:
        print(bcolors.ERROR + "| WakerChecker | Admin" + line.strip() + " is public !")

fn.close()
fichier.close()
browser.close()
