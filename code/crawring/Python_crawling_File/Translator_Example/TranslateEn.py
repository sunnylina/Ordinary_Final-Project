from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

#크롬창 실행
chrome_driver = ChromeDriverManager().install()
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

#파파고 웹페이지 접속
papago_url = "https://papago.naver.com/"
driver.get(papago_url)

#시간적 여유 3초
time.sleep(3)

#작성할 csv파일 생성 -> 변수 'f'에 저장
f = open("./my_papago.csv", "r", encoding="utf-8-sig")

#csv파일 데이터 저장
rdr = csv.reader(f)

#열 제목 건너뜀
next(rdr)

#영어 <-> 한국어 버튼 한번만 클릭
reverse_button = driver.find_element(By.CSS_SELECTOR,"button.btn_switch___x4Tcl").click()

kor = []
#한국어 부분만 따로 저장
for row in rdr:
     kor.append(row[1]) 


for i in kor:

    #단어 입력 -> 번역 버튼 클릭
    form = driver.find_element(By.CSS_SELECTOR,"textarea#txtSource")
    form.send_keys(i)

    button = driver.find_element(By.CSS_SELECTOR,"button#btnTranslate")
    button.click()
    time.sleep(1)

    #번역 결과 저장
    output =  driver.find_element(By.CSS_SELECTOR,"div#txtTarget").text

    print(i, " : ", output)

    #영단어 입력 칸 초기화
    driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").clear()

driver.close()

f.close()