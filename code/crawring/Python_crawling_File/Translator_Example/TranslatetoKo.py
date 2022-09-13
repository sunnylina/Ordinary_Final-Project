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
f = open("./my_papago.csv", "w", newline="", encoding="utf-8-sig")

#csv파일 작성
wtr = csv.writer(f)

#열 제목
wtr.writerow(["영단어","번역결과"])

#무한루프
while True:
    keyword = input("번역할 영단어 입력 (0 입력 시 종료) : ")
    if keyword == "0":
        print("---번역 종료---")
        break

    #영단어 입력 -> 번역 버튼 클릭
    form = driver.find_element(By.CSS_SELECTOR,"textarea#txtSource")
    form.send_keys(keyword)

    button = driver.find_element(By.CSS_SELECTOR,"button#btnTranslate")
    button.click()
    time.sleep(1)

    #번역 결과 저장
    output = driver.find_element(By.CSS_SELECTOR,"div#txtTarget").text

    #my_papago.csv 파일에 [영단어, 번역결과] 작성
    wtr.writerow([keyword, output])

    #영단어 입력 칸 초기화
    driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").clear()

driver.close()

f.close()