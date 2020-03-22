# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊
長，檢查這三個邊長是否可以組成一個三角形。若
可以，則輸出該三角形之周長；否則顯示【Invalid
】。
"""

x = eval(input())
y = eval(input())
z = eval(input())

if x+y > z and x+z > y and y+z > x:
    print(x+y+z)
else:
    print('Invalid')