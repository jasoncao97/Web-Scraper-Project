from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd

import smtplib


URL = 'https://www.amazon.ca/Skybound-Stray-Playstation-4/dp/B0BF622HFH/ref=sr_1_7?crid=RSF4FEO622VG&keywords=ps4+games&qid=1676074604&sprefix=ps4+game%2Caps%2C170&sr=8-7'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Dnt": "1",
    "Connection":"close",
    "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

title = soup1.find(id='productTitle').get_text()
title = title.strip()

price = soup1.find(id='corePrice_feature_div').get_text()
price = price.split('$')[1]

today = datetime.date.today()


# Create CSV 

header = ['Title', 'Price', 'Date']
data = [title, price, today]
 
with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# Appending Data to the CSV

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

# Automate to Check Prices Daily 

def check_price():
    URL = 'https://www.amazon.ca/Skybound-Stray-Playstation-4/dp/B0BF622HFH/ref=sr_1_7?crid=RSF4FEO622VG&keywords=ps4+games&qid=1676074604&sprefix=ps4+game%2Caps%2C170&sr=8-7'

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Dnt": "1",
        "Connection":"close",
        "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    title = soup1.find(id='productTitle').get_text()
    title = title.strip()

    price = soup1.find(id='corePrice_feature_div').get_text()
    price = price.split('$')[1]

    today = datetime.date.today()

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

while(True):
    check_price()
    time.sleep(86400)
