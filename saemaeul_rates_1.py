from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
import datetime
import numpy as np
import pandas as pd

def random_time():
    return random.uniform(0.2, 0.7)

def random_time_2():
    return random.uniform(2.6, 2.8)

def random_time_3():
    return random.uniform(3.4, 3.6)

#계약 기간 (월 단위) 입력
month = 12

#설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
}
options = Options()
options.add_experimental_option("detatch", True)
options.add_argument("--disable-blink-features=AutomationControlled") #강제로 자동화 브라우저가 아님을 말함

#웹사이트 진입
driver = webdriver.Chrome() #executable_path = ''
driver.get("https://www.kfcc.co.kr/map/main.do")
driver.maximize_window() #전체 화면 모드

#광역지역 리스트
metropolitan_list = ["서울", "인천", "경기", "강원", "충남", "충북", "대전", "경북", "경남", "대구", "부산", "울산", "전북", "전남", "광주", "제주"]
#metropolitan_class = ["city01", "city02", "city03", "city04", "city05", "city06", "city07", "city08", "city09", "city10", "city11", "city12", "city13", "city14", "city15", "city16"] 
metropolitan_class = ["city02"]

# 광역지역 버튼 찾아서 위치 반환
def find_metropolitan(mclass):
    mclass_li = driver.find_element(By.CLASS_NAME, mclass)
    mclass_a = mclass_li.find_element(By.TAG_NAME, "a")
    return mclass_a

#Dataframe 만들기
columns = ['광역지역', '군/구', '금고명', '금리']
df = pd.DataFrame(columns=columns)

#핵심 동작
for index, mclass in enumerate(metropolitan_class):
    #광역지역 하나씩 찾아서 클릭
    find_metropolitan(mclass).click()
    driver.implicitly_wait(10)
    time.sleep(random_time())

    metropolitan = metropolitan_list[index - 1] # 광역지역 이름

    #군/구 선택
    gungu_list = driver.find_elements(By.CLASS_NAME, 'btn.small.btn-brown') #버튼 찾음
    for gungu in gungu_list:
        gungu.click()
        driver.implicitly_wait(10)

        #군/구별 금고 리스트에서 금리 버튼 클릭 (파란색 윤곽선)
        gungu_rate_btn_list = driver.find_elements(By.CLASS_NAME, "btn.small.blueBtn03")
        for gungu_rate_btn in gungu_rate_btn_list:
            gungu_rate_btn.click()
            time.sleep(random_time_3()) #페이지 로딩에 약 2.5초 - 2.8초 가량 소요
            
            #거치식예탁금 버튼 클릭
            driver.switch_to.frame('rateFrame2') #금리 안내 테이블은 iframe으로 감싸져 있음.
            yetakgeum_options = driver.find_elements(By.CLASS_NAME, "tabw80")
            geochisik = yetakgeum_options[1]
            geochisik.click()
            time.sleep(random_time_2()) #페이지 로딩에 약 1.5초 - 1.8초 가량 소요
            time.sleep(100)
            driver.switch_to.default_content() #iframe을 나감



    time.sleep(random_time())



