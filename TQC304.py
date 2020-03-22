# -*- coding: utf-8 -*-
"""
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正
整數a，利用迴圈計算從1到a之間，所有5之倍數數
字總和。
"""
a = eval(input())
summ=0
for i in range(1,a+1):
    if i%5==0:
        summ+=i
print(summ)
