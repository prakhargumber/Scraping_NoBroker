import re
from locators.block_locators import BlockLocators


class BlockParser:
    def __init__(self, block):
        self.block = block

    @property
    def id(self):
        return self.block.get_attribute('id')

    @property
    def title(self):
        return str(self.block.find_element_by_css_selector(BlockLocators.TITLE).text)

    @property
    def rent(self):
        rent_maintenance = self.block.find_element_by_css_selector(BlockLocators.RENT_M).text
        regex = '([0-9,]+)'
        match = re.findall(regex, rent_maintenance)
        amount = int(match[0].replace(',', ''))
        return amount

    @property
    def negotiable(self):
        return str(self.block.find_element_by_css_selector(BlockLocators.NEGOTIABLE).text)

    @property
    def possession(self):
        return str(self.block.find_element_by_css_selector(BlockLocators.POSSESS).text)

    @property
    def link(self):
        return self.block.find_element_by_css_selector(BlockLocators.LINK).get_attribute('href')

