import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# todo::get this value from command line
item_id = "01"
# url and search query
item_url = ""
search_query = ""

# load inventory
with open("inventory.json", "r") as read_file:
    inventory_data = json.load(read_file)

for item in inventory_data:
    if (item["id"] == item_id):
        item_url = item["url"]
        search_query = item["search"]["query"]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# webdriver is in local project folder
chrome_driver = os.getcwd() +"\\vendor\\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

# load the url
if(item_url):
    driver.get(item_url)
    soup_file=driver.page_source
    soup = BeautifulSoup(soup_file, features="html.parser")

    print(soup.title.get_text())
    print(soup.find(search_query).get_text())