# -*- coding: utf-8 -*-
"""
 (1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸
入西元年份，然後判斷它是否為閏年（leap year）或
平年。其判斷規則如下：每四年一閏，每百年不閏
，但每四百年也一閏。
 (2) 假設此不定數迴圈輸入-9999則會結束此迴圈。
"""

year = eval(input())

while year!=-9999:
    if year%400==0:
        print('%d is a leap year.'%year)
    elif year%100==0:
        print('%d is not a leap year.'%year)
    elif year%4==0:
        print('%d is a leap year.'%year)
    else:
        print('%d is not a leap year.'%year)
    year = eval(input())
