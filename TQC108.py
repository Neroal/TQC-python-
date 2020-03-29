# -*- coding: utf-8 -*-
"""
設計說明：
 請撰寫一程式，讓使用者輸入四個數字x1、y1、x2
、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計
算並輸出這兩點的座標與其歐式距離。
"""
x1 = eval(input())
x2 = eval(input())
y1 = eval(input())
y2 = eval(input())

print('(%.1f,%.1f)'%(x1,y1))
print('(%.1f,%.1f)'%(x2,y2))

print('Distance = %.4f'%(pow((pow((x1-x2),2)+pow((y1-y2),2)),0.5)))