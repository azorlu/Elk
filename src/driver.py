import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver:
    """Spawns a headless Google Chrome browser"""

    def __init__(self, chrome_driver, is_incognito):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if (is_incognito):
            chrome_options.add_argument("--incognito")
        
        self.browser = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

    def get_page_source(self, url):
        self.browser.get(url)
        return self.browser.page_source