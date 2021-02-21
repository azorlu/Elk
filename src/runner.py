import os
from urllib.parse import urlparse
from .inventor import Inventor
from .driver import Driver
from .html_parser import HtmlParser

class Runner:
    """Scrapes the html and runs the query"""

    def __init__(self, inventory_file, chrome_driver, is_incognito):
        try:
            self.inventory_file = os.getcwd() + inventory_file
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        try:
            self.chrome_driver = os.getcwd() + chrome_driver
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        self.inventor = Inventor(self.inventory_file)
        self.driver = Driver(self.chrome_driver, is_incognito)

    def run_query(self, item_id):
        item = self.inventor.get_item(item_id)
        if (item):
            # check if we are parsing a local file
            parsed_url = urlparse(item.url)
            if (parsed_url.scheme == ''):
                html_parser = HtmlParser(item.url, True)
            else:
                html_parser = HtmlParser(self.driver.get_page_source(item.url))
            return html_parser.find_all(item.query)
        else:
            return "item id does not exist in the inventory file"
    
    def quit(self):
        self.driver.quit()