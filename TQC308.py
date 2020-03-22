# -*- coding: utf-8 -*-
"""
請使用迴圈敘述撰寫一程式，要求使用者輸入一個
數字，此數字代表後面測試資料的數量。每一筆測
試資料是一個正整數（由使用者輸入），將此正整
數的每位數全部加總起來。
"""
datatotalcount = eval(input())
i=0
while i!=datatotalcount:
    num = eval(input())
    temp = num
    summ=0
    while num!=0:
        summ+= num%10
        num//=10
   
    print('Sum of all digits of %d is %d'%(temp,summ))
    i+=1