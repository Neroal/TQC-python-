# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫
函式compute()，此函式接收兩個參數a、b，並回傳
從a連加到b的和。
"""
def compute(a,b):
    ans=0
    for i in range(a,b+1):
        ans+=i
    return ans

x = eval(input())
y = eval(input())

print(compute(x,y))

