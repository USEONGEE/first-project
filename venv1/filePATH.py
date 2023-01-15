# for python

filePATH = input("Type : ")
filePATH = list(filePATH)
new = []
s = ''
for i in filePATH :
    if i == '\\' :
        s = s + '/'
    else :
        s = s + str(i)

print(s)

# for c

# filePATH = input("Type : ")
# filePATH = list(filePATH)
# new = []
# s = ''
# for i in filePATH :
#     if i == '\\' :
#         s = s + "\\\\"
#     else :
#         s = s + str(i)

# print(s)