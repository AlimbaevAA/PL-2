import re

f1= open('access.log' , 'r')
unq=set()

for line in f1.readlines():
    regv = '\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[‌​0-5]|2[0-4][0-9]|[01‌​]?[0-9][0-9]?)\\b'
    IP = re.findall(regv, line)
    for i in range (len(IP)):
        if IP[i] in unq:
            pass
        else:
            unq.add(IP[i])
vv=set()
for item in unq:
    regv = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.)\d{1,3}'
    result = re.findall(regv, item)
    for i in range (len(result)):
        vv.add(result[i])
for el in vv:
    for pi in unq:
        if pi.startswith(el):
            print(pi)
