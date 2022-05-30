from bs4 import BeautifulSoup
from parsers.prop_parser import PropParser


class PropPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def prop(self):
        return PropParser(self.soup)
