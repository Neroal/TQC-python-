# -*- coding: utf-8 -*-
"""
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正
整數（<100），然後以三角形的方式依序輸出此數
的相乘結果。
 提示：輸出欄寬為4，且需靠右對齊。
"""

num = eval(input())

for i in range(1,num+1):   
   for j in range(1,i+1):
       print('%4d'%(i*j),end='')
   print()
           
         

