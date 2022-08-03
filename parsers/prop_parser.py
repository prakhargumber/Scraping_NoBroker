import re
from locators.prop_page_locators import PropLocators


class PropParser:
    def __init__(self, soup):
        self.soup = soup

    @property
    def maintenance(self):
        rent_maintenance = self.soup.select_one(PropLocators.MAINTAIN).text
        regex = '([0-9,]+)'
        match = re.findall(regex, rent_maintenance)
        try:
            amount = int(match[0].replace(',', ''))
        except IndexError:
            amount = 0
        return amount

    @property
    def sq_ft(self):  # int
        return str(self.soup.select_one(PropLocators.SQ_FT).text)

    '''@property
    def deposit(self):  # int
        return str(self.soup.select_one(PropLocators.DEPOSIT).text).strip()'''

    @property
    def age(self):  # categorical
        return str(self.soup.select_one(PropLocators.AGE).text).strip()

    @property
    def posted_on(self):  # date
        return str(self.soup.select_one(PropLocators.POSTED_ON).text).strip()

    @property
    def furnishing(self):  # categorical
        return str(self.soup.select_one(PropLocators.FURNISHING).text)

    @property
    def floor(self):  # categorical
        return str(self.soup.select_one(PropLocators.FLOOR).text)

    @property
    def non_veg(self):  # categorical
        return str(self.soup.select_one(PropLocators.NON_VEG).text)

    @property
    def gated(self):  # categorical
        return str(self.soup.select_one(PropLocators.GATED).text)

    @property
    def maps_location(self):  # str
        lat = str(self.soup.select_one(PropLocators.LATITUDE).attrs['content'])
        long = str(self.soup.select_one(PropLocators.LONGITUDE).attrs['content'])
        return f'https://maps.google.com/?q={lat},{long}'
