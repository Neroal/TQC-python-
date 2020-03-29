# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入兩個正數n、s，代表
正n邊形之邊長為s，計算並輸出此正n邊形之面積（
Area）。
"""
import math
n = eval(input())
s = eval(input())

area = (n*pow(s,2))/(4*math.tan(math.pi/n))

print('Area = %.4f'%area)