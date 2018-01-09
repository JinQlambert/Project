
# coding: utf-8

# In[1]:


#! pip install beautifulsoup4
#! pip install lxml
#! pip install selenium
#! pip install slacker

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


def logintest():
    
    global loginID
    global loginpw

    loginID = input("아이디를 입력해주세요: ")
    loginpw = input("비밀번호를 입력해주세요: ")
    
    print("로그인 테스트를 시작합니다.")


# In[3]:


def testevent():
    global driver
    driver = webdriver.Chrome('Chromedriver') #크롬 드라이버 호출
    driver.implicitly_wait(1) #3초 기다려주기

    url = "https://www.hongik.ac.kr/login.do?Refer=https%3A%2F%2Fhrm.hongik.ac.kr%2Fnew%2Findex.php" #접속 페이지 주소를 미리 변수로 저장
    driver.get(url) 
    
    driver.find_element_by_name('USER_ID').send_keys(loginID)
    driver.find_element_by_name('PASSWD').send_keys(loginpw)
    
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[1]/div[2]/div/table/tbody/tr/td[2]/div/form/div/div/div[2]/button").click()
    
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")


# In[4]:


def Surprise():
    # Random Surprise
    tick = random.randrange(10,50)
    print(tick)

    job = schedule.every(tick).minute
    def attendance():
        RealEvent()
        return schedule.CancelJob

    schedule.every(tick).minute.do(attendance)


def RealEvent():
    testevent()
    
    driver.implicitly_wait(5)
    
    driver.find_element_by_xpath('//*[@id="fm_index1"]/div[2]/div[2]/a').click() #넘어간 페이지에서 출근 버튼 클릭
    
    def checkevent():
    
        url = 'https://hrm.hongik.ac.kr/new/h02/h020100.php' #bs4로 크롤링할 페이지
        driver.get(url)

        html = driver.page_source
    
        soup = BeautifulSoup(html, 'lxml')
    
        attendancelist = soup.find("div", {"class": "table0"}).find_all("tr")
    
        today_attendance = attendancelist[7].text #오늘날짜 출근여부
        
        token = 'xoxb-295111285623-xMQ4NxaJ722POUyyN1DKCGeh'
        slack = Slacker(token)
        slack.chat.post_message('#general', today_attendance)
        
    checkevent()


# In[5]:


logintest()
testevent()


# In[33]:


YesOrNoTest = input("오류가 없었나요?:[y/n] ")


# In[39]:


if YesOrNoTest == "y":
    print("프로그램 작동을 시작합니다")
    schedule.every().day.at("8:00").do(Surprise)
else :
    print("오류를 해결한 후 다시 로그인 테스트를 해주세요(비밀번호 확인 및 변경)")
    quit()


# In[40]:


if __name__ == "__main__":
	while True:
		schedule.run_pending()
		time.sleep(1)

