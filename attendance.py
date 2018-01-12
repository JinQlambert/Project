
# coding: utf-8

# In[3]:


def RealEvent():
    testevent(driver, loginID, loginpw)
    driver.implicitly_wait(5)  
    driver.find_element_by_xpath('//*[@id="fm_index1"]/div[2]/div[2]/a').click() #넘어간 페이지에서 출근 버튼 클릭
    driver.find_element_by_xpath('//*[@id="aside"]/ul/li[2]/ul/li[1]/a').click() #출근부 클릭
    return schedule.CancelJob
    
def GetAttendance():
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    attendancelist = soup.find("div", {"class": "table0"}).find_all("tr")
    today_attendance = attendancelist[7].text #오늘날짜 출근여부
    return today_attendance

def Attendance(driver):
    # Random Surprise
    tick = random.randrange(10,40)
    print(tick)
        
    schedule.every(tick).minutes.do(RealEvent) #parallel로 작성하려다가 출석이 안되었는데 내용을 긁어오게 될까봐 둘로 나누어보았어요
    schedule.every(41).minutes.do(GetAttendance)