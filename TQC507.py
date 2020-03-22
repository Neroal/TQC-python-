# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入一個整數x，並將x傳
遞給名為compute()的函式，此函式將回傳x是否為質
數（Prime number）的布林值，接著再將判斷結果
輸出。如輸入值為質數顯示【Prime】，否則顯示【
Not Prime】。
"""

def compute(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
        
    return True

x = eval(input())

if compute(x):
    print('Prime')
else:
    print('Not Prime')
