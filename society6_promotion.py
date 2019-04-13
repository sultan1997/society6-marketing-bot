from selenium import webdriver
import time
import random
import os


'''type_comments = [] 
with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'society6comments.txt'), 'rt') as in_file:
 for line in in_file: 
   type_comments.append(line.rstrip('\n'))''' 
   

driver = webdriver.Chrome()
driver.get("https://society6.com/login?done=/")
username = driver.find_element_by_id('email')
username.send_keys("exp4money@gmail.com")
password = driver.find_element_by_id('password')
password.send_keys("sultan1997")
driver.find_element_by_name('login').click()

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

type_comments = ['Amazing Art!', 'Great Work!', 'Awesome!', 'Cool', 'Promoted :)', 'looks so cool :O', 'Like the way it feel']
print(type_comments)

for i in range(50):
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

