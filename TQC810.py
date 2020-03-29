# -*- coding: utf-8 -*-
"""
請撰寫一程式，首先要求使用者輸入正整數k（1 <=
k <= 100），代表有k筆測試資料。每一筆測試資料
是一串數字，每個數字之間以一空白區隔，請找出
此串列數字中最大值和最小值之間的差。
 提示：差值輸出到小數點後第二位。
"""

n = 0
while n <1 or n>100:
    n = eval(input())

for i in range(n):
    string = input().split(' ')
    LIST=[]
    for j in range(len(string)):
        LIST.append(eval(string[j]))
    print('%.2f'%((max(LIST)-min(LIST))))
    
    

