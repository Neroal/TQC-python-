# -*- coding: utf-8 -*-
"""
請撰寫一程式，輸入數個整數並儲存至串列中，以
輸入-9999為結束點（串列中不包含-9999），再將此
串列轉換成數組，最後顯示該數組以及其長度（
Length）、最大值（Max）、最小值（Min）、總和
（Sum）。
"""
LIST = []

num = eval(input())
while num!=-9999:
    LIST.append(num)
    num = eval(input())
TUPLE = tuple(LIST)
print(TUPLE)
print('Lenght:',len(TUPLE))
print('Max:',max(TUPLE))
print('min:',min(TUPLE))
