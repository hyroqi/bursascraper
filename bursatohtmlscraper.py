from helium import *
from bs4 import BeautifulSoup
import time

# HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
URL = "https://www.bursamalaysia.com/market_information/announcements/company_announcement"

#starting browser
browser = start_chrome(URL, headless=True)
time.sleep(5)

#fetching full html data
html = browser.page_source
soup = BeautifulSoup(html, "lxml")

#fetching table data
tableOdd = soup.findAll('tr', class_ = "odd") # table-compact table table-striped text-center ann-table text-default js-anchor-ann-table dataTable no-footer
tableEven = soup.findAll('tr', class_ = "even")

#writing to file
f = open("soup.html", "w")
for odd_row, even_row in zip(tableOdd, tableEven):
    print(odd_row, file=f)
    print(even_row, file=f)
f.close()


##plan is to get the hrefs from the odd and even row shit, then access those one by one, pull the data out and then append it to the end of its respective
##odd or even line
