# This program can find duplication of data.
# This program handles only txt_file.
# This program is made by 'shdbtjd8@gachon.ac.kr'
# If you have any question, mail above address
# Have a nice day :)

# hard coding 정리해야됨

fileName = input('Type file name : ')

#################

file ='C:/Users/shdbt/Desktop/DATAFILE/조방/'
file = file + fileName +'.txt'
r = open(file,'r') # file 불러오기
lines = r.readlines() # file을 line 단위로 가져와 list로 저장
len_lines = len(lines)

################## 

# lines = [] 
# file = 'C:/Users/shdbt/Desktop/DATAFILE/result'
# for i in range(24) :
#     r = open(file + str(i+1) +'.txt','r')
#     line = r.readlines()
#     lines += line
# len_lines = len(lines)

###################

## error data 색출
li = []

for i in range(len_lines -1):
    if(lines[i] == lines[i+1]):
        print('index ' + str(i) + ' has a duplication data.')
        j = str(i)
        li.append(j) # 오류가 있는 index를 li에 저장, 오류 index는 0부터 시작
        
## save data that is set, index of missing

w = open('C:/Users/shdbt/Desktop/DATAFILE/조방/ex.txt','w')

for i in li :
    w.write(i + '\n')
    
w.close()