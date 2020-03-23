# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內
容為從鍵盤輸入的整數（不重複），接著輸出矩陣
最大值與最小值的索引。
"""

list1 = []
for i in range(3):
    list1.append([])
    for j in range(3):
        list1[i].append(eval(input()))
        
max_index = min_index = [0,0]
maxn = minn = list1[0][0]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        if minn > list1[i][j]:
            minn = list1[i][j]
            min_index=[i,j]
        elif maxn < list1[i][j]:
            maxn = list1[i][j]
            max_index=[i,j]
print('Index of Max number',maxn,'is:',max_index)
print('Index of min number',minn,'is:',min_index)