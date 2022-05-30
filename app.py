import time
import requests
import pandas as pd

from selenium import webdriver
from pages.query_page import QueryPage
from pages.prop_page import PropPage

chrome = webdriver.Chrome()
chrome.get('https://www.nobroker.in/property/rent/gurgaon/Landmark%20Avenue?searchParam=W3sibGF0IjoyOC40NTE3NzQxLCJsb24iOjc3LjA4NjA2MjUwMDAwMDAxLCJwbGFjZUlkIjoiQ2hJSnc4WlRPTWNZRFRrUm5Hb3A3U1RqZjdvIiwicGxhY2VOYW1lIjoiTGFuZG1hcmsgQXZlbnVlIn1d&radius=7.0&sharedAccomodation=0&city=gurgaon&locality=Landmark%20Avenue&orderBy=lastUpdateDate,desc&type=BHK2&rent=5000,25000&leaseType=BACHELOR&furnishing=SEMI_FURNISHED&buildingType=AP&bathroom=2')

time.sleep(60)

last_height = chrome.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(1)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = chrome.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#
#     last_height = new_height

# chrome.execute_script("""
#         function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));}
#         let str = `div[itemtype="http://schema.org/Apartment"]`;
#         let count = parseInt(document.getElementById('propertyCount'));
#
#         while (true){
#             const element = document.querySelectorAll(str);
#             if (element.length > count){break;}
#             element[element.length - 1].scrollIntoView(false);
#             await sleep(4000);
#         }
# """)

# response_time = page.elapsed
# page_dt = page.headers['Date']

# print(response_time)
# print(page_dt, '\n')

query = QueryPage(chrome)

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
    # print(i, '\n')

    # print(f'Property Area: {prop_page.sq_ft}')
    # print(f'Deposit: {prop_page.deposit}')
    # print(f'Furnishing: {prop_page.furnishing}')
    # print(f'maintenance: {prop_page.maintenance}')
    print(i, '\n')
    i += 1

df = pd.DataFrame(list(zip(furnish, prop_id, title, rent,
                           maintain, link, posted_on, possess,
                           age, floor, non_veg, gated, maps_loc)),
                  columns=['Furnishing', 'ID', 'Title', 'Rent', 'Maintenance', 'Link',
                           'Posted on', 'Possession', 'Age of property', 'Floor number', 'Non-veg',
                           'Gated Security', 'Maps Location'])

file_name = "Gurugram_2bhk_Apartment_Semi_25K_7km" + ".csv"
df.to_csv(file_name, index=False)
print("File Exported Sucessfully!!!!")
