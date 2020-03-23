# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入四週各三天的溫度，
接著計算並輸出這四週的平均溫度及最高、最低溫
度。
"""

weektemp=[]

for i in range(4):
    weektemp.append([])
    print('Week ',i+1,':')
    for j in range(3):
        print('Day',j+1,end=':')
        weektemp[i].append(eval(input()))
        
sum_temp = []
for i in range(4):
    sum_temp.extend(weektemp[i])
    
print('Average %.2f'%(sum(sum_temp)/12))
print('Height %.2f'%(max(sum_temp)))
print('Lowest %.2f'%(min(sum_temp)))
