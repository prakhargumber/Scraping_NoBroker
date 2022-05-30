from locators.query_page_locators import QueryPageLocators
from parsers.block_parser import BlockParser


class QueryPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def blocks(self):
        return [
            BlockParser(b)
            for b in self.browser.find_elements_by_css_selector(
                QueryPageLocators.BLOCK
            )
        ]
