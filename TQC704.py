# -*- coding: utf-8 -*-
"""
請撰寫一程式，輸入數個整數並儲存至集合，以輸
入-9999為結束點（集合中不包含-9999），最後顯示
該集合的長度（Length）、最大值（Max）、最小值
（Min）、總和（Sum）。
"""

set1 = set()

num = eval(input())
while num!=-9999:
    set1.add(num)
    num = eval(input())

print('Lenght:',len(set1))
print('Max:',max(set1))
print('min:',min(set1))
print('Sum:',sum(set1))
