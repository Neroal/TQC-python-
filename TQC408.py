# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入十個整數，計算並輸
出偶數和奇數的個數。
"""
oddcount=0
evencount=0

for i in range(10):
    num = eval(input())
    if num%2==0:
        evencount+=1
    else:
        oddcount+=1
print('Even numbers: %d'%evencount)
print('Odd numbers: %d'%oddcount)
