# -*- coding: utf-8 -*-
"""
請撰寫一程式，依照使用者輸入的n，畫出對應的等
腰三角形。
"""

n = eval(input())

for i in range(1,n+1):
    for j in range(0,n-i):
        print(' ',end='')
    for k in range((2*i)-1):
        print('*',end='')
    print()
