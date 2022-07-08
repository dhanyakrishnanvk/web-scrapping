#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pip install selenium


# In[3]:


import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[5]:


driver=webdriver.Chrome("/usr/local/bin/chromedriver")


# In[14]:


driver=webdriver.Chrome("chromedriver")
time.sleep(2)


# In[111]:


driver.get("https://www.naukri.com/")


# In[112]:


search_designation=driver.find_element_by_class_name("suggestor-input")
search_designation.send_keys("Data Analyst")
search_location=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
search_location.send_keys("Bangalore")
search_button=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
search_button.click()


# In[113]:


job_title=[]
job_location=[]
company_name=[]
experience=[]
##title=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']"):
    job_title.append(i.text)
job_title[0:10]
for i in driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']"):
    company_name.append(i.text)
company_name[0:10]
for i in driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span"):
    experience.append(i.text)
experience[0:10]
for i in driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]"):
    job_location.append(i.text)
job_location[0:10]    
jobs=pd.DataFrame()
jobs['Job_Title']=job_title
jobs['Company']=company_name
jobs['Experience']=experience
jobs['Location']=job_location
jobs[0:10] 


# In[108]:


driver.get("https://www.naukri.com/")


# In[109]:


search_designation=driver.find_element_by_class_name("suggestor-input")
search_designation.send_keys("Data Scientist")
search_location=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
search_location.send_keys("Bangalore")
search_button=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
search_button.click()


# In[110]:


job_title=[]
job_location=[]
company_name=[]
experience=[]
##title=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']"):
    job_title.append(i.text)
job_title[0:10]
for i in driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']"):
    company_name.append(i.text)
company_name[0:10]
for i in driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span"):
    experience.append(i.text)
experience[0:10]
for i in driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]"):
    job_location.append(i.text)
job_location[0:10]    
jobs=pd.DataFrame()
jobs['Job_Title']=job_title
jobs['Company']=company_name
jobs['Experience']=experience
jobs['Location']=job_location
jobs[0:10] 


# In[17]:


driver.get("https://www.flipkart.com/")
login=driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
try:
    login.click
except:
    pass


# In[18]:


search_sunglasses=driver.find_element_by_class_name("_3704LK")
search_sunglasses.send_keys("sunglasses")


# In[19]:


search_button=driver.find_element_by_class_name("_34RNph")
search_button.click()


# In[32]:


for i in range(3):
    from selenium.common.exceptions import ElementNotInteractableException
try:
    next_button=driver.find_element_by_xpath("//span[@class='_22Tduf']")
    next_button.click()
except ElementNotInteractableException as e:
    print("Exception Raised",e)
    next_button=driver.find_element_by_xpath("//a[@class='ge-49M']")
    driver.get(next_button.get_attribute('href'))
    time.sleep(5) 
Brand=[]
for i in driver.find_elements_by_xpath("//div[@class='_2WkVRV']"):
    Brand.append(i.text)
description=[]
for i in driver.find_elements_by_xpath("//a[@class='IRpwTa']"):
    description.append(i.text)
price=[]
for i in driver.find_elements_by_xpath("//div[@class='_30jeq3']"):
    price.append(i.text)       
sunglasses=pd.DataFrame()
sunglasses['Brand']=Brand
sunglasses['description']=description
sunglasses['Price']=price
sunglasses


# In[179]:


driver.get("https://www.flipkart.com/")


# In[207]:


search=driver.find_element_by_class_name("_3704LK")
search.send_keys("Iphone11")
search_button=driver.find_element_by_class_name("_34RNph")
search_button.click()
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZE3ENS&marketplace=FLIPKART&q=Iphone11&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=97f2789a-6842-41a7-aa11-7ccf420b3fd0.MOBFWQ6BXGJCEYNY.SEARCH&ppt=sp&ppn=sp&ssid=2udu55ykj40000001656591445650&qH=6d60e39954c2077c")
all_reviews=driver.find_element_by_xpath("//div[@class='_3UAT2v _16PBlm']")
all_reviews.click()


# In[222]:



for i in range(10):
    rating=[]
for i in driver.find_elements_by_xpath("//div[@class='_3LWZlK _1BLPMq']"):
    rating.append(i.text)
rating
description=[]
for i in driver.find_elements_by_xpath("//p[@class='_2-N8zT']"):
    description.append(i.text)
brief=[]
for i in driver.find_elements_by_xpath("//div[@class='t-ZTKy']"):
    brief.append(i.text)
next_button=driver.find_element_by_xpath("//span[@class='_22Tduf']")
next_button.click()
time.sleep(5)
   
reviews=pd.DataFrame()
reviews['Rating']=rating
reviews['description']=description
reviews['Brief']=brief
reviews[0:100]


# In[33]:


driver.get("https://www.myntra.com/shoes")


# In[ ]:




