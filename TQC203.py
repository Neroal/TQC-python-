# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個西
元年份，然後判斷它是否為閏年（leap year）或平年
。其判斷規則為：每四年一閏，每百年不閏，但每
四百年也一閏。
"""
year = eval(input())

if year%400 == 0 :
    print('%d is a leqp year'%year)
elif year%100 == 0:
    print('%d is not a leqp year'%year)
elif year%4==0:
    print('%d is a leqp year'%year)
else:
    print('%d is not a leqp year'%year)