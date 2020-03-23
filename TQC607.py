# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入三位學生各五筆成績
，接著再計算並輸出每位學生的總分及平均分數。
 提示：平均分數輸出到小數點後第二位。
"""

data = []

for i in range(3):
    print('The %d student:'%(i+1))
    data.append([])
    for j in range(5):
        data[i].append(eval(input()))

for i in range(3):
     print('Student %d:'%(i+1))
     print('Sum %d'%(sum(data[i])))
     print('Average %.2f'%(sum(data[i])/len(data[i])))
     
     
         