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
excelFilePath = 'C:/Users/shdbt/Desktop/22년도 학술제/부산_중구_노인복지시설.xlsx'
sheet = '부산_중구_노인복지시설'

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
response = requests.get(url)
def get_cordinate() :
     html = driver.page_source
     soup = BeautifulSoup(html, 'lxml')
     content = soup.select('#result')
     print(content)
     content = str(content)
     strlist.append(content)

# pyautogui.mouseInfo()
# F12 제일 작게 하고 가로 1000,1242
def control_mouse():
    pyautogui.moveTo(753,745)
    sleep(1)
    pyautogui.click()
    sleep(2)

# Load data from excel file
def getExcelData(FilePath, sheetName, startCell, endCell) : # All parameter types are 'String',
    load_wb = load_workbook(FilePath, data_only = True)
    load_ws = load_wb[sheetName]
    get_cells = load_ws[startCell : endCell]
    
    data = []
    for row in get_cells:
        for cell in row :
            data.append(cell.value)
            
    return data # cell을 저장한 list를 반환함.

# 데이터가 담긴 list를 parameter로 받아 100개 단위로 나누어 2D_list를 만들어 반환한다.  // data가 100개 이하 일 경우 아래 함수를 사용 x
def separateData_by100(data): 
    len_ = int(len(data)/100)
    li = []
    if(len(data) % 100 != 0) :
        len_ += 1
    for i in range(len_ - 1) :
        childList = data[i*100 : (i+1)*100 -1]
        li.append(childList)
    childList = data[len_*100 : ]
    li.append(childList)
    print("there are {}_list.".format(len_))
    
    return li

excelData = getExcelData(excelFilePath,sheet)


# //CROWLING//

number = int(input('type a number under or same len_\n'))
fileName = '중구_노인복지시설'
fileNumber = number
final_fileName = fileName + str(fileNumber) +'.txt'

for i,letter in enumerate(excelData): #excelData_separated[number]
    if(i==0) :
        input_search(letter)
        sleep(10)
        control_mouse()
        get_cordinate()
    else :
        input_search(letter)
        control_mouse()
        get_cordinate()

# 저장
file = open(final_fileName, 'w') # exception 발생시 'x' 를 'w' 로 수정해서 사용할 것
for i in strlist :
    file.write(i + '\n')

file.close()