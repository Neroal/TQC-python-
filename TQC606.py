# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入兩個正整數rows、cols
，分別表示二維串列lst 的「第一個維度大小」與「
第二個維度大小」。串列元素[row][col]所儲存的數
字，其規則為：row、col 的交點值 = 第二個維度的
索引col – 第一個維度的索引row。接著以該串列作
為參數呼叫函式compute()輸出串列。
 提示：欄寬為4。
"""
def compute(rows,cols):
    for i in range(rows):
        list1.append([])
        for j in range(cols):
            list1[i].append(j-i)  
            print('%4d'%list1[i][j],end='')
        print()

list1=[]

rows = eval(input())
cols = eval(input())

compute(rows,cols)

