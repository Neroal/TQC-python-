# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入一個正整數，將此數
值以反轉的順序輸出
"""

num = eval(input())

while num!=0:
    print(num%10,end='')
    num//=10