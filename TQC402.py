# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入數字，輸入的動作直
到輸入值為9999才結束，然後找出其最小值，並輸
出最小值。

"""
LIST = []

while True:
        value = eval(input())
        if value == 9999:
            break
        LIST.append(value)
print(min(LIST))