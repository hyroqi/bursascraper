from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import time

#URL to scrape
URL = "https://www.bursamalaysia.com/market_information/announcements/company_announcement"

#start browser
browser = start_chrome(URL, headless=True)
time.sleep(5)

#get the HTML content
html = browser.page_source
soup = BeautifulSoup(html, "lxml")

#find all table rows
rows = soup.find_all('tr')

#initialize lists to store data
data = []

#extract text from each row and remove tags
for row in rows:
    row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
    data.append(row_data)

#convert data into a DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

#export DataFrame to Excel
df.to_excel("output.xlsx", index=False)

#close browser
kill_browser()