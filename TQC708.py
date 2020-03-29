# -*- coding: utf-8 -*-
"""
請撰寫一程式，自行輸入兩個詞典（以輸入鍵值
"end"作為輸入結束點，詞典中將不包含鍵值"end"）
，將此兩詞典合併，並根據key值字母由小到大排序
輸出，如有重複key值，後輸入的key值將覆蓋前一
key值。
"""
xDIC={}
yDIC={}

print('Create dict1:')

while True:
    key = input('Key:')
    if key == 'end':
        break
    xDIC[key] = input('Value:')
    
print('Create dict2:')

while True:
    key = input('Key:')
    if key == 'end':
        break
    yDIC[key] = input('Value:')
    
xDIC.update(yDIC)

for i in sorted(xDIC.keys()):
    print(i,': ',xDIC[i])
