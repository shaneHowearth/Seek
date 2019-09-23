#!/usr/bin/env python3

import time
from lxml import html
import requests
from os import system, name 

# Settings
MAXRESULTS = 3
WAIT = 300 # In seconds
# Programming language you are searching for (eg. java, python, golang)
SEARCH = "golang"

# Seek have set values that can be searched on for the salary amount
salaryValues = ["0", "30000", "40000", "50000", "60000", "70000", "80000", "100000", "120000", "150000", "200000", "999999"]
SALMIN = salaryValues[8]
SALMAX = salaryValues[-1]

locations = ["All-Australia-AU", "All-New-Zealand", "London-UK", "All-Auckland", "All-Waikato", "All-Wellington", "All-Canterbury", "Western-Australia-WA-AU"]
LOCATION = locations[0]

# Clear the terminal
def clear(): 
    # for windows 
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else:
        _ = system('clear')

# Page to be scraped
link = "https://www.seek.co.nz/"+SEARCH+"-jobs/in-"+LOCATION+"?salaryrange="+SALMIN+"-"+SALMAX+"&salarytype=annual&sortmode=ListedDate"

def scrapeSeek():
    # Get page data from server, block redirects
    response = requests.get(link)

    dom = html.fromstring(response.content)

    # loop over results
    for advertList in dom.xpath('//*[@data-automation="searchResults"]/div/div[2]'):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        for advert in advertList.xpath('div')[:MAXRESULTS]:
            # Headline and advertiser
            try:
                advertiser = advert.xpath('article/span[5]/span/a/text()')[0]
            except IndexError:
                advertiser = advert.xpath('article/span[5]/span/span[2]/text()')[0]

            print("http://www.seek.co.nz"+advert.xpath('article/span[2]/span/h1/a')[0].get("href"))
            print(advert.xpath('article/span[2]/span/h1/a/text()')[0], " : ",advertiser)

            # Blurb
            print(advert.xpath('article/span[6]/span/text()')[0])

            # Location
            city = advert.xpath('article/div/span[2]/span/strong/span/span/text()')[0]
            city = city.split(":")[1].strip()
            try:
                suburb = advert.xpath('article/div/span[2]/span/span/span/text()')[0]
                suburb = suburb.split(":")[1].strip()
            except IndexError:
                suburb = ""
            print(city+" / " +suburb)
            # Salary
            try:
                print(advert.xpath('article/div/span[3]/span/text()')[0])
            except IndexError:
                print("No salary provided.")
            # Age of ad
            print("Listed: "+advert.xpath('article/span[4]/span/span/text()')[0])
            print("---========---\n")

# Infinite loop
while True:
    clear()
    scrapeSeek()
    time.sleep(WAIT)
