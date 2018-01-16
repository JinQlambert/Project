
# coding: utf-8

# In[ ]:


import random
import schedule
from bs4 import BeautifulSoup
from login import loginsequence
from slackto import send


# In[ ]:


def RealEvent(driver, loginID, loginpw, token):
    loginsequence(driver, loginID, loginpw)
    driver.implicitly_wait(3)  
    driver.find_element_by_xpath('//*[@id="fm_index1"]/div[2]/div[2]/a').click()#넘어간 페이지에서 출근 버튼 클릭
    driver.find_element_by_xpath('//*[@id="aside"]/ul/li[2]').click() #출근부 버튼 클릭
    driver.find_element_by_xpath('//*[@id="aside"]/ul/li[2]/ul/li[1]/a').click() #출근부 클릭
    message = "출석버튼이 눌러졌어요!"
    if token == 'n':
        pass
    else :
        print(message)
        send(token, message)
    return schedule.CancelJob
    
def GetAttendance(driver, token):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    attendancelist = soup.find("div", {"class": "table0"}).find_all("tr")
    message = attendancelist[7].text #오늘날짜 출근여부
    if token == 'n':
        pass
    else :
        print(message)
        send(token, message)


# In[25]:


def Attendance(driver, loginID, loginpw, token):
    # Random Surprise
    tick = random.randrange(10,40)
    print(tick)
        
    schedule.every(tick).minutes.do(RealEvent, driver, loginID, loginpw, token) #parallel로 작성하려다가 출석이 안되었는데 내용을 긁어오게 될까봐 둘로 나누어보았어요
    schedule.every(41).minutes.do(GetAttendance, driver, token)

