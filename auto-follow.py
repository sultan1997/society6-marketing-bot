from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://society6.com/login?done=/")
username = driver.find_element_by_id('email')
username.send_keys("exp4money@gmail.com")
password = driver.find_element_by_id('password')
password.send_keys("sultan1997")
driver.find_element_by_name('login').click()

accounts_scrapped = ['https://society6.com/andrejpopa', 'https://society6.com/kerriganmcknz', 'https://society6.com/bledsusuri']

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
