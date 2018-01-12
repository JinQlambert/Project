
# coding: utf-8

# In[1]:


get_ipython().system(' pip install selenium')

import random
import time

import schedule

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Surprise():
	# Random Surprise
	tick = random.randrange(10,50)
	print(tick)

	job = schedule.every(tick).minute
	def attendance(job):
		schedule.jobs.remove(job)
		RealEvent()

	job.do(attendance, job)


schedule.every().day.at("8:00").do(Surprise)


def RealEvent():

    
    driver = webdriver.Chrome('C:\\Users\\JinQ Kim\\Chromedriver') #크롬 드라이버 호출, py로 바꿔서는 경로 재설정
    driver.implicitly_wait(3) #3초 기다려주기

    url = "https://www.hongik.ac.kr/login.do?Refer=https%3A%2F%2Fhrm.hongik.ac.kr%2Fnew%2Findex.php" #접속 페이지 주소를 미리 변수로 저장
    driver.get(url) 
    
    driver.find_element_by_name('USER_ID').send_keys('loginid')
    driver.find_element_by_name('PASSWD').send_keys('loginpw')
    
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[1]/div[2]/div/table/tbody/tr/td[2]/div/form/div/div/div[2]/button").click() #로그인 버튼을 클릭해보자
    
    driver.implicitly_wait(5)
    
    driver.find_element_by_xpath('//*[@id="fm_index1"]/div[2]/div[2]/a').click() #넘어간 페이지에서 출근 버튼 클릭

if __name__ == "__main__":
	while True:
		schedule.run_pending()
		time.sleep(1)

