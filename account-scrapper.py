import time
import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

r = requests.get('https://society6.com/discover')
print(r.status_code)
r.raise_for_status()

soup = BeautifulSoup(r.content, "html.parser")
a_tags = soup.find_all("a", attrs={"class": "author track"})

discover_accounts = []

for a in a_tags:
    discover_accounts.append(a['href'])

print(discover_accounts)
print("number of discovered account: " + str(len(discover_accounts)))

accounts_scrapped = []
counter = 1
a = 0

while a <= len(discover_accounts):
    source = requests.get('https://society6.com/api/users' + discover_accounts[a] + '/followers?page=%s' % counter).json()
    if source['data']['attributes']['followers']:
        for i in source['data']['attributes']['followers']:
            print("added: https://society6.com" + i['card']['link']['href'] + " on page: " + str(counter) )
            accounts_scrapped.append("https://society6.com" + i['card']['link']['href'])
        counter += 1
        print("next page")
    else:
        a += 1
        counter = 0
        print("next account to scrap: " + accounts_scrapped[a + 1])
    print("current account scrapping: " + accounts_scrapped[a] + " , on page: " + str(counter))
    print("currently scrapped accounts: " + str(len(accounts_scrapped)))
    
print("total accounts scrapped: " + str(len(accounts_scrapped)))

'''
accounts_scrapped = []
counter = 1

while True:
    source = requests.get('https://society6.com/api/users/babecat/followers?page=%s' % counter).json()
    if source['data']['attributes']['followers']:
        for i in source['data']['attributes']['followers']:
            print("https://society6.com" + i['card']['link']['href'])
            accounts_scrapped.append("https://society6.com" + i['card']['link']['href'])
        counter += 1
    else:
        break     

print("Number of accounts scrapped: " + str(len(accounts_scrapped)))'''

