from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://society6.com/login?done=/")
username = driver.find_element_by_id('email')
username.send_keys(" ")        #input your username here
password = driver.find_element_by_id('password')
password.send_keys(" ")        #input your password here
driver.find_element_by_name('login').click()
