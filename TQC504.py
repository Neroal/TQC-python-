# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫
函式compute()，此函式接收兩個參數a、b，並回
傳 的值。
"""
def compute(a,b):
    return pow(a,b)

x = eval(input())
y = eval(input())
print(compute(x,y))

