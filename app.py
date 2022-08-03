import time
import requests
import pandas as pd

from datetime import date
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.query_page import QueryPage
from pages.prop_page import PropPage

chrome = webdriver.Chrome(ChromeDriverManager().install())

chrome.get('https://www.nobroker.in/property/rent/gurgaon/Fabindia%20Vipul%20Golf%20Course%20EC?searchParam=W3sibGF0IjoyOC40NTk3MDI5LCJsb24iOjc3LjA5NTYyODEsInBsYWNlSWQiOiJDaElKN1otUVY0UVpEVGtSWXJXRnJPdmJPMzAiLCJwbGFjZU5hbWUiOiJGYWJpbmRpYSBWaXB1bCBHb2xmIENvdXJzZSBFQyIsInNob3dNYXAiOmZhbHNlfV0=&sharedAccomodation=0&city=gurgaon&locality=Fabindia%20Vipul%20Golf%20Course%20EC&type=BHK3&rent=20000,46000&furnishing=FULLY_FURNISHED,SEMI_FURNISHED&bathroom=2&radius=6.5&orderBy=availableFrom,asc&buildingType=AP&withPics=1')

chrome.execute_script("""
        function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));}

        async function Scroll() {
            let str = `div[itemtype="http://schema.org/Apartment"]`;
            const count = parseInt(document.getElementById('propertyCount').textContent);

            while (true){
                const element = document.querySelectorAll(str);
                if (element.length >= count){break;}
                element[element.length - 1].scrollIntoView(false);
                await sleep(1500);
            }
        }
        Scroll();
""")

time.sleep(6)

query = QueryPage(chrome)
while len(query.blocks) < query.blocks_num:
    time.sleep((query.blocks_num - len(query.blocks)) / 4)
    query = QueryPage(chrome)

st = time.time()
pst = time.process_time()

cols = ['Furnishing', 'ID', 'Title', 'Link', 'Rent', 'Negotiation',
        'Maintenance', 'Property Area(sq_ft)', 'Posted on', 'Possession', 'Floor',
        'Age of property', 'Non-veg', 'Gated security', 'Maps location']
df = pd.DataFrame(columns=cols)

i = 1
for block in query.blocks:
    time.sleep(0.4)  # one request every half a second
    page = requests.get(block.link).content
    prop_page = PropPage(page).prop

    df.loc[i] = (prop_page.furnishing, block.id, block.title, block.link, block.rent,
                 block.negotiable, prop_page.maintenance, prop_page.sq_ft,
                 prop_page.posted_on, block.possession, prop_page.floor, prop_page.age,
                 prop_page.non_veg, prop_page.gated, prop_page.maps_location)

    print(i, '\n')
    i += 1

today = date.today()
file_name = "Gurugram_3bhk_AP_46K_6.5km_" + f"{today.strftime('%d_%m')}" + ".csv"
df.to_csv(f'csv_datasets\\{file_name}', index=False)
print("File Exported Sucessfully!")

pet = time.process_time()
et = time.time()
print(f'Elapsed process time: {pet-pst} and Elapsed time: {et-st}')
