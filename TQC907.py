"""
請撰寫一程式，要求使用者輸入檔名read.txt，顯示
該檔案的行數、單字數（簡單起見，單字以空白隔
開即可，忽略其它標點符號）以及字元數（不含空
白）。
"""

filename = input()

file = open('./database/'+filename,'r',encoding='UTF-8')

linec = wordc = charc = 0

for line in file:
    linec+=1
    SPLIT = line.split(' ')
    wordc+=len(SPLIT)
    for i in range(len(SPLIT)):
        charc += len(SPLIT[i])

print(linec,' line(s)')
print(wordc,'word(s)')
print(charc,'char(s)')

file.close()
