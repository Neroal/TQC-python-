# -*- coding: utf-8 -*-
"""
請撰寫一程式，利用一維串列存放使用者輸入的12
個正整數（範圍1~99）。顯示這些數字，接著將串
列索引為偶數的數字相加並輸出結果。
 提示：輸出每一個數字欄寬設定為3，每3個一列，
靠右對齊。
"""

list1 = []
size=12
for i in range(1,size+1):
    list1.append(eval(input()))
total=0
for i in range(1,size+1):
    if i%3==0:
        print('%3d'%(list1[i-1]))
    else:
        print('%3d'%list1[i-1],end='')
    if (i-1)%2==0:
        total+=list1[i-1]
print(total)

