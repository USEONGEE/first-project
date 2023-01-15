# This program can process data
# This program can handle only 'txt file'
# This program is made by 'shdbtjd8@gachon.ac.kr'
# If you have any question, mail above address
# Have a nice day :)

fileName = input('Type : ')
path = 'C:/Users/shdbt/Desktop/DATAFILE/조방/'
fileName = path + fileName +'.txt'

r = open(fileName,'r')

lines = r.readlines() # array

lat = []
long = []

## String에서 필요한 element를 찾음
def findElement(value):
    start1 = value.find('.') - 2
    end1 = value.find(',')
    start2 = value.find(',') + 6
    end2 = value.find('입') - 2
    indexOfelement = [start1,end1,start2,end2]

    return indexOfelement

## data_Processing
for line in lines :
    indexOfelement = findElement(line)
    latitude = line[indexOfelement[0] : indexOfelement[1] + 1]
    longtitude = line[indexOfelement[2]: indexOfelement[3] + 1]
    lat.append(latitude)
    long.append(longtitude)

r.close()

## 결과 저장
corSet = zip(lat,long)
corSet = list(corSet)

a = open(path + 'DATA.txt','w')


for i in corSet :
    cordinate = str(i[0]) + str(i[1])
    a.write(cordinate + '\n')

a.close()

