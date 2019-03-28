import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url="https://www.hubertiming.com/results/2018MLK"
html=urlopen(url)

soup = BeautifulSoup(html, features="html.parser")

# Get title of the page
#title = soup.title
#print(title)
#print(title.text)

#Get all links on the page
#links = soup.find_all('a', href=True)
#for link in links:
#    print(link['href'])


# Get info in table
data = []
allrows = soup.find_all("tr")
for row in allrows:
    row_list = row.find_all("td")
    dataRow = []
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)
data = data[4:]


df = pd.DataFrame(data)
#print(df.head(2))
#print(df.tail(2))

header_list = []
col_headers = soup.find_all('th')
for col in col_headers:
    header_list.append(col.text)

df.columns = header_list
# first 2 lines
#print(df.head(2))

# get info about table
#df.info()
#df.shape

df = df.dropna(how='any')

df['ChipTime_minutes'] = pd.to_timedelta(df['Chip Time'])
df['ChipTime_minutes'] = df['ChipTime_minutes'].astype('timedelta64[s]') / 60
#print(df[['Gender', 'ChipTime_minutes']].head())

# Create graph
plt.bar(df['Gender'],df['ChipTime_Minutes'])
#plt.xlabel('Gender')
#plt.ylabel('ChipTime_Minutes')
#plt.title("Cimparison of average minutes run by male and female")
