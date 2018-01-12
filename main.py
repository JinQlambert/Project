
# coding: utf-8

# In[1]:


import random
import time
import schedule

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.request import urlopen
from slacker import Slacker


# In[2]:


from login import login_prompt, loginsequence
from attendance import RealEvent, GetAttendance, Attendance  


# In[3]:


driver = webdriver.Chrome('Chromedriver')
loginID, loginpw = login_prompt()
loginsequence(driver, loginID, loginpw)


# In[ ]:


schedule.every().day.at("8:00").do(Attendance)
    
if __name__ == "__main__":
        while True:
                schedule.run_pending()
                time.sleep(1)

