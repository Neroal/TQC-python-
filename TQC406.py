# -*- coding: utf-8 -*-
"""
請撰寫一程式，以不定數迴圈的方式輸入身高與體
重，計算出BMI之後再根據以下對照表，印出BMI
及相對應的BMI代表意義（State）。假設此不定數
迴圈輸入-9999則會結束此迴圈。
"""

height = eval(input())

while height != -9999:
    weight = eval(input())
    if weight != -9999:
        bmi = weight/(pow(height/100,2))
        print('BMI:%.2f'%bmi)
        if bmi < 18.5:
            print('State:under weight')
        elif 18.5 <= bmi <25:
            print('State:normal')
        elif 25 <= bmi <30:
            print('State:over weight')
        elif 30 <= bmi:
            print('State:fat')
    else:
        break
    height = eval(input())
    