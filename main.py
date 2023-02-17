import os, random, time, json, itertools
from selenium import webdriver
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class Viewbot:
    def __init__(self):
        self.config = json.load(open('./data/config.json', 'r+'))
        self.proxies = itertools.cycle(open('./data/proxies.txt').read().splitlines())
        self.ua = UserAgent()

    def ui(self):
        os.system('cls && title View-Bot' if os.name == "nt" else 'clear')
        print(f"""{Fore.BLUE}
        (`-.              ('-.    (`\ .-') /`        .-. .-')                .-') _
      _(OO  )_          _(  OO)    `.( OO ),'        \  ( OO )              (  OO) )
  ,--(_/   ,. \ ,-.-') (,------.,--./  .--.           ;-----.\  .-'),-----. /     '._
  \   \   /(__/ |  |OO) |  .---'|      |  |     .-')  | .-.  | ( OO'  .-.  '|'--...__)
   \   \ /   /  |  |  \ |  |    |  |   |  |,  _(  OO) | '-' /_)/   |  | |  |'--.  .--'
    \   '   /,  |  |(_/(|  '--. |  |.'.|  |_)(,------.| .-. `. \_) |  |\|  |   |  |
     \     /__),|  |_.' |  .--' |         |   '------'| |  \  |  \ |  | |  |   |  |
      \   /   (_|  |    |  `---.|   ,'.   |           | '--'  /   `'  '-'  '   |  |
       `-'      `--'    `------''--'   '--'           `------'      `-----'    `--'
        {Fore.RESET}""")
        print(f"""{Fore.CYAN}
        View-Bot Starting...
        {Fore.RESET}""")

    def open_url(self, ua, sleep_time, proxy):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument('--start-maximized')
        self.options.add_argument('user-agent=%s' % ua.random)
        self.options.add_argument("--proxy-server=%s" % proxy)
        self.options.headless = True

        self.browser = uc.Chrome(options=self.options)

        self.browser.get(self.config["url"])
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        time.sleep(sleep_time)
        self.browser.quit()

    def main(self):
        self.ui()
        for _ in range(self.config["views"]):
            self.sleeptime = random.randint(self.config["min_watch"], self.config["max_watch"])
            self.open_url(self.ua, self.sleeptime, next(self.proxies))

if __name__ == "__main__":
    bot = Viewbot()
    bot.main()
