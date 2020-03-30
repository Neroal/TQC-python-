# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整
數a、b，然後再輸入一算術運算子 (+、-、*、/、//
、%） ，輸出經過運算後的結果。
"""

a = eval(input())
b = eval(input())
operator = input()

if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
elif operator == '//':
    print(a//b)
elif operator == '%':
    print(a%b)
