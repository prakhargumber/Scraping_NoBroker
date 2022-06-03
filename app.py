import time
import requests
import pandas as pd

from selenium import webdriver
from pages.query_page import QueryPage
from pages.prop_page import PropPage

chrome = webdriver.Chrome()
chrome.get('https://www.nobroker.in/property/rent/gurgaon/Landmark%20Avenue?searchParam=W3sibGF0IjoyOC40NTE3NzQxLCJsb24iOjc3LjA4NjA2MjUwMDAwMDAxLCJwbGFjZUlkIjoiQ2hJSnc4WlRPTWNZRFRrUm5Hb3A3U1RqZjdvIiwicGxhY2VOYW1lIjoiTGFuZG1hcmsgQXZlbnVlIn1d&radius=4.0&sharedAccomodation=0&city=gurgaon&locality=Landmark%20Avenue&orderBy=lastUpdateDate,desc&type=BHK2&rent=5000,25000&leaseType=BACHELOR&furnishing=SEMI_FURNISHED&buildingType=AP&bathroom=2')

time.sleep(3)

chrome.execute_script("""
        function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));}

        async function Scroll() {
            let str = `div[itemtype="http://schema.org/Apartment"]`;
            const count = parseInt(document.getElementById('propertyCount').textContent);

            while (true){
                const element = document.querySelectorAll(str);
                if (element.length >= count){break;}
                element[element.length - 1].scrollIntoView(false);
                await sleep(2000);
            }
        }
        Scroll();
""")

time.sleep(5)

while True:
    query = QueryPage(chrome)
    if len(query.blocks) >= query.blocks_num:
        break
    time.sleep(4)

prop_id = []
title = []
rent = []
negotiate = []
maintain = []
link = []
posted_on = []
possess = []
age = []
floor = []
non_veg = []
gated = []
maps_loc = []
furnish = []

i = 1
for block in query.blocks:
    page = requests.get(block.link).content
    prop_page = PropPage(page).prop

    furnish.append(prop_page.furnishing)
    prop_id.append(block.id)
    title.append(block.title)
    rent.append(block.rent)
    negotiate.append(block.negotiable)
    maintain.append(prop_page.maintenance)
    link.append(block.link)
    posted_on.append(prop_page.posted_on)
    possess.append(block.possession)
    age.append(prop_page.age)
    floor.append(prop_page.floor)
    non_veg.append(prop_page.non_veg)
    gated.append(prop_page.gated)
    maps_loc.append(prop_page.maps_location)

    # print(f'Property Area: {prop_page.sq_ft}')
    # print(f'Deposit: {prop_page.deposit}')

    print(i, '\n')
    i += 1

df = pd.DataFrame(list(zip(furnish, prop_id, title, rent,
                           maintain, link, posted_on, possess,
                           age, floor, non_veg, gated, maps_loc)),
                  columns=['Furnishing', 'ID', 'Title', 'Rent', 'Maintenance', 'Link',
                           'Posted on', 'Possession', 'Age of property', 'Floor number', 'Non-veg',
                           'Gated Security', 'Maps Location'])

file_name = "Gurugram_2bhk_Apartment_Semi_25K_4km" + ".csv"
df.to_csv(file_name, index=False)
print("File Exported Sucessfully!")
