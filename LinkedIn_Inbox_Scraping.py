import time
import re
from selenium import webdriver

# Browser
driver = webdriver.Chrome() # Optional argument, if not specified will search path.
driver.get(‘https://www.linkedin.com/login')

nameidElem = driver.find_element_by_id(‘username’)
nameidElem.send_keys(‘*****@gmail.com’)

pwdidElem = driver.find_element_by_id(‘password’)
pwdidElem.send_keys(‘*******’)
continueElem = driver.find_element_by_class_name(“btn__primary — large”) 
result=continueElem.submit()

time.sleep(10)

messagesElem = driver.find_element_by_id(“messaging-tab-icon”) 
messagesElem.click()

sender_email_list=[]
current_edit=[]
current_edit_cum=[]
for i in range(0,10):
  print(i)  
  current=driver.find_elements_by_class_name("msg-conversation-listitem__participant-names")
  current_edit_cum=current_edit_cum+current_edit
  current_edit=list(set(current) - set(current_edit_cum))
  for person in current_edit:
      person.click()
      print(person.text)
      time.sleep(5)
      for text in driver.find_elements_by_class_name("msg-s-event-listitem__body"):
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text.text)
        if emails!=[]:
            sender_email_list=sender_email_list+[emails]
            time.sleep(10)
  person.click()
  scroll=driver.find_element_by_tag_name('html')
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  scroll.send_keys(Keys.DOWN)
  
import numpy as np
sender_email_list=np.unique(sender_email_list)
list_subject=pd.DataFrame(list(sender_email_list))
list_subject.to_csv('C:\\Users\\User\\Downloads\\linkedin_list.csv',index=False)
