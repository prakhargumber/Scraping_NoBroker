import re
import numpy as np
from locators.block_locators import BlockLocators


class BlockParser:
    def __init__(self, block):
        self.block = block

    @property
    def id(self):
        return str(self.block.get_attribute('id'))

    @property
    def title(self):
        return str(self.block.find_element_by_css_selector(BlockLocators.TITLE).text)

    @property
    def rent(self):
        rent_maintenance = self.block.find_element_by_css_selector(BlockLocators.RENT_M).text
        regex = '([0-9,]+)'
        match = re.findall(regex, rent_maintenance)
        try:
            amount = int(match[0].replace(',', ''))
        except IndexError:
            amount = np.nan  # To account for any text value present inplace of the amount
        return amount

    @property
    def negotiable(self):
        return str(self.block.find_element_by_css_selector(BlockLocators.NEGOTIABLE).text)

    @property
    def possession(self):
        return str(self.block.find_element_by_css_selector(BlockLocators.POSSESS).text)  # Date format

    @property
    def link(self):
        return str(self.block.find_element_by_css_selector(BlockLocators.LINK).get_attribute('href'))
