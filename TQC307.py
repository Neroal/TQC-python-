# -*- coding: utf-8 -*-
"""
(1) 請使用迴圈敘述撰寫一程式，要求使用者輸入一
個正整數n（n<10），顯示n*n乘法表。
 (2) 每項運算式需進行格式化排列整齊，每個運算子
及運算元輸出的欄寬為2，而每項乘積輸出的欄寬為
4，皆靠左對齊不跳行。
"""

n = eval(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print('%-2d%-2c%-2d%-2c%-4d'%(j,'*',i,'=',(j*i)),end='')
    print()