# -*- coding: utf-8 -*-
"""
請撰寫一程式，要求使用者輸入十個數字並存放在
串列中。接著由大到小的順序顯示最大的3個數字。
"""

SIZE = 10
num = []
for i in range(SIZE):
    num.append(eval(input()))
    
num.sort()

print('%d %d %d'%(num[-1],num[-2],num[-3]))
