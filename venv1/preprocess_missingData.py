# This program can process missing data (N/A) and input data.
# This program handles only txt_file
# This program is made by 'shdbtjd8@gachon.ac.kr'
# If you have any question, mail above address.
# Have a nice day :)

# 각각의 파일을 불러와 한 파일에 합치기
# 파일명 : lowData.txt

file = 'C:/Users/shdbt/Desktop/DATAFILE/result'

content = []


# parameter : 파일명
# 파일을 받아 내용을 content 안에 삽입
def readFile(filename) :
    cont = []
    r = open(filename,'r')
    lines = r.readlines()
    for i in lines :
        char_int = i.find('\\')
        i = i[0:char_int]
        cont.append(i)
    r.close()
    return cont
    
# 이어붙일 파일 연결
a = open('C:/Users/shdbt/Desktop/DATAFILE/lowData.txt','a')

# main file에 content 삽입 = all result_file 합치기
for i in range(22) :
    fileName = file + str(i+1) + '.txt'
    content = readFile(fileName)
    for j in content :
        a.write(j + '\n')
    content = []
        
a.close()
    