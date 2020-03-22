# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個正
整數，然後判斷它是否為偶數（even）。
"""
number = eval(input(''))

if number%2 == 0:
    print('%d is an even number'%number)
else:
    print('%d is not an even number'%number)