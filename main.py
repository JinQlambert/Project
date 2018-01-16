# coding: utf-8

# In[1]:


import time
import schedule

from selenium import webdriver


# In[2]:


from login import login_prompt, loginsequence
from attendance import Attendance  


# In[3]:


driver = webdriver.Chrome('Chromedriver')
loginID, loginpw, token = login_prompt()
loginsequence(driver, loginID, loginpw)


# In[ ]:


YesOrNoTest = input("오류가 없었나요?:[y/n] ")
if YesOrNoTest =="y":
    print("프로그램을 시작합니다")
    print("윈도우 업데이트 등 자동 종료가 되지않도록 해주세요")
    driver.quit()
    
    schedule.every().day.at("8:00").do(Attendance, driver, loginID, loginpw, token)
else :
    print("프로그램을 종료합니다.")
    print("오류를 해결 한 후 프로그램을 다시 실행해주세요")
    driver.quit()
    time.sleep(3)
    quit()
    
if __name__ == "__main__":
        while True:
                schedule.run_pending()
                time.sleep(1)

