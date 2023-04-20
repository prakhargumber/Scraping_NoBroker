# Scraping Real Estate data from NoBroker
Building a Web Scraper with Python to extract live real estate property data hosted on nobroker.in. [NoBroker](https://www.nobroker.in/) is a real estate listings platform that provides brokerage-free properties on rent/sale.


https://user-images.githubusercontent.com/90957886/233464167-7527c416-e377-4b5e-8cc1-e3ea9bb1b30d.mp4


Have a look at the [output file](csv_datasets/Gurugram_3bhk_AP_46K_6.5km_03_08.csv)

Navigation:
/locators - Find CSS selectors used to scrape specific elements from different pages of the website
/parsers - To parse each property listing information as a block
/pages - To input html content of a webpage and parse it using parsers
app.py - Scraper to scroll through the webpage and implement objects to output a csv file containing clean scraped data
