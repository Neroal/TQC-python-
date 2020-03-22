# -*- coding: utf-8 -*-
"""
請撰寫一程式，由使用者輸入十個數字，然後找出
其最小值，最後輸出最小值。
"""
num = [0,0,0,0,0,0,0,0,0,0]


for i in range(len(num)):
    num[i] = eval(input())
    
print(min(num))