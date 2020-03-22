# -*- coding: utf-8 -*-
"""
請撰寫一程式，將使用者輸入的三個整數（代表一
元二次方程式 的三個係數a、b、c）作
為參數傳遞給一個名為compute()的函式，該函式回
傳方程式的解，如無解則輸出【Your equation has no
root.】
"""

def compute(a,b,c):
    if (pow(b,2)-(4*a*c)) < 0:
        print('You question has no solution!')
        return None
    else:
        ans1 = (-b+(pow(pow(b,2)-(4*a*c),0.5)))/(2*a)
        ans2 = (-b-(pow(pow(b,2)-(4*a*c),0.5)))/(2*a)
        return str(ans1)+','+str(ans2)

a = eval(input())
b = eval(input())
c = eval(input())

print(compute(a,b,c))


