# -*- coding: utf-8 -*-
"""
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正
整數n，利用迴圈計算並輸出n!的值。
"""

n = eval(input())
ans =1

for i in range(1,n+1):
    ans*=i

print(ans)