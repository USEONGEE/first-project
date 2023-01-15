# This program can crawling data (cordinate of each address) from "http://map.esran.com/"
# Caution : Using this program may be illegal
# This program is made by 'shdbtjd8@gachon.ac.kr'
# If you have any question, mail above address.
# Have a nice day :)

from selenium import webdriver
from bs4 import BeautifulSoup
# needed in "chromedriver new version package"
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from time import sleep
import requests
import pyautogui
import lxml  # parser
from array import array

# map.erason으로 찾기

url = 'http://map.esran.com/'
driver_path = 'chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(url)

sleep(3)

# form 형성
keyboard_form = driver.find_element(By.ID, 'keyword')
search_form = driver.find_element(
    By.XPATH, '//*[@id="main"]/div[1]/div/div/article/section[1]/form/button')

# 값을 받을 변수
strlist = []  # crowling된 값은 받음
excelData = []  # excelData를 받음

# 검색어 입력, 검색


def input_search(keyword):
    try:
        for i in range(30):
            keyboard_form.send_keys(Keys.BACKSPACE)
        keyboard_form.send_keys(keyword)
        search_form.send_keys(Keys.ENTER)
    except:
        print('auto-mouse error but keep going')


# soup, instance 화
response = requests.get(url)


def get_cordinate():
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    content = soup.select('#result')
    print(content)
    content = str(content)
    strlist.append(content)

# 마우스 포인트 위치 940,648 (전체화면 기준, 모니터별 상이)
# pyautogui.mouseInfo()
# F12 제일 작게 하고 가로 1000px, ALL px, 배율 50%


def control_mouse():
    pyautogui.moveTo(805, 735)
    sleep(1)
    pyautogui.click()
    sleep(2)


# excel file 가져오기
load_wb = load_workbook(
    "C:/Users/shdbt/Desktop/DATAFILE/policeStation.xlsx", data_only=True)  # csv 지원 x
load_ws = load_wb['DATA']  # sheet 이름


get_cells = load_ws['C2':'C2310']
for row in get_cells:
    for cell in row:
        excelData.append(cell.value)

# missingData의 index 가져오기
r = open('C:/Users/shdbt/Desktop/DATAFILE/indexOfmissingData.txt', 'r')
lines = r.readlines()  # array # 개행문자 존재

new_lines = []  # 개행문자 제거
for i in lines:
    ind = i.find('\\')
    j = i[0:ind]
    new_lines.append(int(j))

# missingData의 low_data, excel에서 가져오기
missingList = []

print(excelData[3])

for i in new_lines:
    childList = excelData[i]  # index는 0부터 시작
    missingList.append(childList)

# missingData_list를 100개 단위로 분할
# generalization 필요
mL1 = missingList[0:100]
mL2 = missingList[100:200]
mL3 = missingList[200:]

# //CROWLING AND SAVING TO FILE//
file = open("C:/Users/shdbt/Desktop/DATAFILE/missingData3", 'w')

strlist = []
for i, letter in enumerate(mL3):
    if (i == 0):
        input_search(letter)
        sleep(20)
        control_mouse()
        get_cordinate()
    else:
        input_search(letter)
        control_mouse()
        get_cordinate()


for i in strlist:
    file.write(i + '\n')

file.close()
