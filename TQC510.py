# -*- coding: utf-8 -*-
"""
請撰寫一程式，計算費氏數列（Fibonacci numbers）
，使用者輸入一正整數num (num>=2)，並將它傳遞
給名為compute()的函式，此函式將輸出費氏數列前
num個的數值。
"""

def compute(n): 
    curr = 1
    pre = 0
    print(0,1,end=' ')
    for i in range(2,n):
        temp = curr+pre
        print(temp,end=' ')
        pre = curr
        curr = temp
        
num = eval(input())

compute(num)
        
