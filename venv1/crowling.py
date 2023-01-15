# This program can crawling data (cordinate of each address) from "http://map.esran.com/"
# Caution : Using this program may be illegal
# This program is made by 'shdbtjd8@gachon.ac.kr'
# If you have any question, mail above address.
# Have a nice day :)

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By # needed in "chromedriver new version package"
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from time import sleep
import requests
import pyautogui
import lxml # parser
from array import array


# map.erason으로 찾기

url = 'http://map.esran.com/'
driver_path = 'chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(url)

sleep(3)

# form 형성
keyboard_form = driver.find_element(By.ID,'keyword')
search_form = driver.find_element(By.XPATH,'//*[@id="main"]/div[1]/div/div/article/section[1]/form/button')

# 값을 받을 변수
strlist =[] # crowling된 값은 받음
excelData =[] # excelData를 받음

# 검색어 입력, 검색
def input_search(keyword):
    try :
        for i in range(30) :
            keyboard_form.send_keys(Keys.BACKSPACE)
        keyboard_form.send_keys(keyword)
        search_form.send_keys(Keys.ENTER)
    except :
        print('error but keep going')

# soup, instance 화
def get_cordinate() :
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    content = soup.select('#result')
    print(content)
    content = str(content)
    strlist.append(content)

# pyautogui.mouseInfo()
# F12 제일 작게 하고 가로 1000px, ALL px, 배율 50%
def control_mouse():
    pyautogui.moveTo(805,731)
    sleep(1)
    pyautogui.click()
    sleep(2)

# excel file 가져오기
load_wb = load_workbook("C:/Users/shdbt/Desktop/DATAFILE/조방/policeStation.xlsx",data_only=True) # csv 지원 x
load_ws = load_wb['DATA'] # sheet 이름

get_cells = load_ws['C2' :'C2310']
for row in get_cells:
    for cell in row :
        excelData.append(cell.value)

# 크롤링 분할 진행을 위해 low data 분할하기
# ex) list[0] == excelData[0:100], list[1] == excelData[100:200] etc.

# test_sep = excelData[0:15]
list = []
n = 100
for i in range(24):
    if i == 23 :
        childList = excelData[n*i :]
        list.append(childList)
    else :
        childList = excelData[n*i : (i+1)*n]
        list.append(childList)

# //CROWLING//

number = int(input('Type number of a index you want to find, but less or equal 23 \n'))
fileName = 'result'
fileNumber = number + 1
final_fileName = fileName + str(fileNumber) +'.txt'

# //this line has a simple problem, PAY ATTENTION "UNDER REMARK"//
file = open(final_fileName, 'x') # exception 발생시 'x' 를 'w' 로 수정해서 사용할 것

for i,letter in enumerate(list[number]):
    if(i==0) :
        input_search(letter)
        sleep(20)
        control_mouse()
        get_cordinate()
    else :
        input_search(letter)
        control_mouse()
        get_cordinate()

# 저장

for i in strlist :
    file.write(i + '\n')

file.close()
