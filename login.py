
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# In[5]:


def login_prompt():
    loginID = input("아이디를 입력해주세요: ")
    loginpw = input("비밀번호를 입력해주세요: ")
    
    print("로그인 테스트를 시작합니다.")
    
    return (loginID, loginpw)


# In[6]:


def loginsequence(driver, loginID, loginpw):
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
   
