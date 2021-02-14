import json
from bs4 import BeautifulSoup

class HtmlParser:
    """Parses html using Beautiful Soup"""

    def __init__(self, page_source):
        self.html = BeautifulSoup(page_source, features="html.parser")

    def get_html(self):
        return self.html
    
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
    # find_all(name, attrs, recursive, string, limit, **kwargs)
    def find_all(self, query):
        result = self.html.find_all(query.name, string=query.string)
        return result