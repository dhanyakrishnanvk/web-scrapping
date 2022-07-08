#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pip install selenium


# In[33]:


import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time
from selenium.common.exceptions import InvalidSelectorException                  


# In[4]:


driver=webdriver.Chrome("/usr/local/bin/chromedriver")


# In[6]:


driver.get("https://www.amazon.in")


# In[7]:


shoes=driver.find_element_by_id("twotabsearchtextbox")
shoes.send_keys("shoes")


# In[8]:


search=driver.find_element_by_id("nav-search-submit-button")
search.click()


# In[44]:


start=0
end=4
for page in range(start,end):
    Brand=[]
for i in driver.find_elements_by_class_name("s-line-clamp-1"):
    Brand.append(i.text)
Brand
nxt_button=driver.find_elements_by_xpath("//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")#scraping the list of buttons from the page

try:

        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page

except:

        driver.get(nxt_button[0].get_attribute('href')) 
        
description=[]
for i in driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div[2]/h2/a/span"):
    description.append(i.text)

price=[]
for i in driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div[4]/div/a/span[1]/span[2]/span[2]"):
    price.append(i.text)
data=pd.DataFrame()
data['Brand']=Brand
data['price']=price
data['description']=description
data(0,100)


# In[ ]:





# In[ ]:




