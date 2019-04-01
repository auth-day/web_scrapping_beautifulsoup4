import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url',
                        '-u',
                        default='https://www.hubertiming.com/results/2018MLK',
                        help="Url to parse")

    args = parser.parse_args()
    url = args.url
    html=urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")

    data = gather_data(soup)
    draw_graph(header_update(soup,data))


def gather_data(soup):
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
    return df

def header_update(soup, df):
    header_list = []
    col_headers = soup.find_all('th')
    for col in col_headers:
        header_list.append(col.text)
    df.columns = header_list
    return df

def draw_graph(updated_data):
    df = updated_data.dropna(how='any')

    df['ChipTime_Minutes'] = pd.to_timedelta(df['Chip Time'])
    df['ChipTime_Minutes'] = df['ChipTime_Minutes'].astype('timedelta64[s]') / 60

    # Create graph compare gender
    plt.bar(df['Gender'], df['ChipTime_Minutes'])
    plt.xlabel('Gender')
    plt.ylabel('ChipTime_Minutes')
    plt.title("Cimparison of average minutes run by male and female")
    plt.show()

if __name__ == '__main__':
    main()
