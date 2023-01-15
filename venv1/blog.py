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

url = 'https://admin.blog.naver.com/AdminMain.naver?blogId=girl0316&Redirect=BuddyMe'
driver_path = 'chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(url)

sleep(10)
# value = []
count = 2

selector_front = '#wrap > div:nth-child(4) > table > tbody > tr:nth-child('
selector_back = ') > td.buddy > div > div > span.nickname'


def get_soup(url_) :
    res = requests.get(url_)
    print(res.status_code)
    if res.status_code == 200:            
        return BeautifulSoup(res.text, 'html.parser')
    else :
        print("no return")
        return None

def get_content(soup_,selector_) :
    content = soup_.select(selector_).text # 여기에 문제가 있다.
    print(content)

selector = selector_front + str(count) + selector_back
print(selector)
soup = get_soup(url)
get_content(soup, selector) 