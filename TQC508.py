# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入兩個正整數x、y，並
將x與y傳遞給名為compute()的函式，此函式回傳x和
y的最大公因數。
"""
def  compute(x,y):
    gcd = 1  
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd        
    
x,y = eval(input())
print(compute(x,y))
