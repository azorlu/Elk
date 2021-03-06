import json
from bs4 import BeautifulSoup
from .query_type import QueryType
from .query import Query

class HtmlParser:
    """Parses html using Beautiful Soup"""

    def __init__(self, page_source, is_local_file=False):
        if (is_local_file):
            with open(page_source, 'r') as f:
                data = f.read()
            self.html = BeautifulSoup(data, features="html.parser")
        else:
            self.html = BeautifulSoup(page_source, features="html.parser")

    def get_html(self):
        return self.html
    
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
    # find_all(name, attrs, recursive, string, limit, **kwargs)
    def find_all(self, query):
        return self.find_all_by_query_type(query)
    
    def find_all_by_query_type(self, query):
        if (query.query_type & QueryType.NAME_STRING):
            result = self.html.find_all(query.name, string= query.string)
        elif (query.query_type & QueryType.NAME):
            result = self.html.find_all(query.name)
        elif (query.query_type & QueryType.STRING):
            result = self.html.find_all(string=query.string)
        else:
            # return an empty array for non-implemented query types
            return [] 
        return result