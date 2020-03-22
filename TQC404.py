# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入一個正整數，將此正
整數以反轉的順序輸出，並判斷如輸入0，則輸出為
0。
"""
num = eval(input())

if num == 0:
    print(0)
else:
    while(num!=0):
        print('%d'%(num%10),end='')
        num//=10
