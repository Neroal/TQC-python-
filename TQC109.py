# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入一個正數s，代表正五
邊形之邊長，計算並輸出此正五邊形之面積(Area)。
"""
import math

slength = eval(input())

area = (5*pow(slength,2))/(4*math.tan(math.pi/5))

print('Area = %.4f'%area)
