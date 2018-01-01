
# coding: utf-8

# In[13]:


get_ipython().system(' pip install selenium')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[15]:


def logintest():

    loginID = input("아이디를 입력해주세요: ")
    loginpw = input("비밀번호를 입력해주세요: ")
    
    print("로그인 테스트를 시작합니다.")
    
    driver = webdriver.Chrome('C:\\Users\\JinQ Kim\\Chromedriver') #크롬 드라이버 호출
    driver.implicitly_wait(3) #3초 기다려주기

    url = "https://www.hongik.ac.kr/login.do?Refer=https%3A%2F%2Fhrm.hongik.ac.kr%2Fnew%2Findex.php" #접속 페이지 주소를 미리 변수로 저장
    driver.get(url) 
    
    driver.find_element_by_name('USER_ID').send_keys(loginID)
    driver.find_element_by_name('PASSWD').send_keys(loginpw)
    
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[1]/div[2]/div/table/tbody/tr/td[2]/div/form/div/div/div[2]/button").click() #로그인 버튼을 클릭해보자


# In[16]:


logintest()


# In[12]:


YesOrNoTest = input("로그인이 추가 팝업창 또는 오류 없이 되었나요?[y/n]")

