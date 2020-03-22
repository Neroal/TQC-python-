# -*- coding: utf-8 -*-
"""
請撰寫一程式，以不定數迴圈的方式輸入一個正整
數（代表分數），之後根據以下分數與GPA的對照
表，印出其所對應的GPA。假設此不定數迴圈輸入9999則會結束此迴圈。
"""
num = eval(input())

while num!=9999:
    if 90<= num <=100:
        print('A')
    elif 80 <= num <=89:
        print('B')
    elif 70 <= num <=79:
        print('C')
    elif 60 <= num <=69:
        print('D')
    elif 0 <= num <=59:
        print('E')
    else:
        print('Error!')
    num = eval(input())
        
