from selenium import webdriver
import time
import random
import os

driver.find_element_by_link_text('My Society').click()
driver.find_element_by_link_text('Discover').click()

promote_button = driver.find_elements_by_class_name('promoteButton')
add_comments = driver.find_elements_by_class_name('add') 
comments = driver.find_elements_by_xpath("//form[@class='addComment']//textarea[contains(@placeholder,'Add a comment')]") 
submit_comments = driver.find_elements_by_xpath("//button[text()='Comment']")  

#print(len(add_comments))
#print(len(comments))
#print(len(submit_comments))
#print(len(promote_button))

type_comments = ['Amazing Art!', 'Great Work!', 'Awesome!', 'Cool', 'Promoted :)', 'looks so cool :O', 'Like the way it feel'] #Edit the comments here
print(type_comments)

for i in range(50): #change the number of time the bot comments on the page
      promote_button[i].click()
      print("liked")
      time.sleep(2)
      print("comment begins")
      add_comments[i].click()
      print("+add comment clicked")
      time.sleep(2)
      comments[i].click()
      print("comment textbox clicked")
      time.sleep(2)
      comments[i].send_keys(random.choice(type_comments))
      print("text typed")
      time.sleep(2)
      submit_comments[i].click()
      print("comment submited")
      time.sleep(2)

