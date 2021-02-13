from bs4 import BeautifulSoup

class HtmlParser:
    """Parses html using Beautiful Soup"""

    def __init__(self, page_source):
        self.html = BeautifulSoup(page_source, features="html.parser")

    def get_html(self):
        return self.html