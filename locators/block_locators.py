class BlockLocators:
    TITLE = 'span[class="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full"]'  # .string
    RENT_M = '#minimumRent'  # .text will get 'Rs. Rent + Maintenance'
    NEGOTIABLE = '#minDeposit div.heading-7'  # .string
    POSSESS = 'div[class="flex p-0.5p items-center"] div[class="flex flex-1 pl-0.5p"] div div.font-semibold'
    LINK = '#exploreNearbuy'  # .get('href')
