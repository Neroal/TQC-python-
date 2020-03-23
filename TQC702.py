# -*- coding: utf-8 -*-
"""
請撰寫一程式，輸入並建立兩組數組，各以-9999為
結束點（數組中不包含-9999）。將此兩數組合併並
從小到大排序之，顯示排序前的數組和排序後的串
列。
"""

tuple1 = ()

print('Create tuple 1:')
num = eval(input())

while num !=-9999:
    tuple1 +=(num,)
    num = eval(input())
tuple2 = ()
print('Create tuple 2:')
num = eval(input())
while num !=-9999:
    tuple2 +=(num,)
    num = eval(input())
tuple1 += tuple2

print('Combined tuple before sorting:',tuple1)

LIST = list(tuple1)
LIST.sort()

print('Combined list after sorting:',LIST)