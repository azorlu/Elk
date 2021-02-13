# Main program entry
import os
from inventor import Inventor
from driver import Driver
from html_parser import HtmlParser

inventory_file = os.getcwd() + "\\inventory.json"
chrome_driver = os.getcwd() +"\\driver\\chromedriver.exe"

inventor = Inventor(inventory_file)
driver = Driver(chrome_driver, False)

# simple test run
test_id = "02"
html_parser = HtmlParser(driver.get_page_source(inventor.get_item(test_id).url))
#print(html_parser.get_html().get_text())
print(html_parser.get_html().title.get_text())