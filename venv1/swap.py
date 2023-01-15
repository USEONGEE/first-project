# crowling data에 N/A가 존재했음.
# 'crowling_missingData' 를 통해 결츨값에 대한 data를 확보
# result(1~24)의 data와 missing_data를 병합해 전처리를 하고자 한다.


fileName = "result" # filename 을 얻기 위한 str 변수
path = 'C:/Users/shdbt/Desktop/DATAFILE/' # 파일 저장 위치


data = [] # file data 가 index를 가지고 저장됨 (key : index, value : content)
indexingData = {} # {index : value}, index 범위 [0~2308]

def getContent(filename) : # parameter : 경로를 포함한 file, return값은 file의 내용 (datatype : list)
    r = open(filename,'r')
    lines = r.readlines()
    return lines

def getFilePath(path, file_name) : # parameter : 경로, 파일명 (.txt 제외)
    fullname = path + file_name +'.txt'
    return fullname

for i in range(24) :
    file = getFilePath(path, fileName + str(i+1)) 
    lines = getContent(file)
    data = data + lines

for index, value in enumerate(data) :
    indexingData[index] = value # 

## 모든 result data를 하나의 파일로 합치기
# filena = path + 'final_result.txt'
# w = open(filena, 'w')
# for dat in data :
#     w.write(str(dat)) # data입력시 입력 후 개행문자까지 입력된다.

## missingData 불러오기

fileName2 = 'missingData' 
mdata = []
indexingMdata = {}

for i in range(3) :
    file = getFilePath(path, fileName2 + str(i+1))
    lines = getContent(file)
    mdata = mdata + lines

## missing data, dictonary 만들기

index = getContent(path + 'indexOfmissingData.txt')
index = index[0:-1]
for i in range(len(index)) : # index의 element들이 str 이므로 int형으로 수정 (사유 : file data에 개행문자가 더해져있음.)
    index[i] = int(index[i])
tmp = zip(index,mdata)
indexingMdata = dict(tmp)   

##### 현재 진행 상황, indexingData -> 전체 데이터, indexingMdata -> 결측값 데이터, excel 기준으로 index라벨링까지 완료

for i in indexingData :
    for j in indexingMdata :
        if i == j : 
            indexingData[i+1] = indexingMdata[i]
            
## 전처리가 끝난 데이터, txt_file 로 저장

filena = path + 'afterAllProcessing.txt'
w = open(filena, 'w')
for dat in indexingData :
    w.write(str(indexingData[dat])) # data입력시 입력 후 개행문자까지 입력된다. key error 수정 요망

