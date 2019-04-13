from selenium import webdriver
import time

accounts_scrapped = [] #empty list which take accounts scrapped as input

for follow in accounts_scrapped:
    driver.get(follow)
    try:
        follow_button = driver.find_element_by_xpath("//span[text() = 'Follow']")
        print("found follow button")
        follow_button.click()
        print("followed")
    except:
        print("already followed this account. Going to next one")
        continue
