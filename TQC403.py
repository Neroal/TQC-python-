# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入兩個正整數a、b（
a<=b），輸出從a到b（包含a和b）之間4或9的倍數
（一列輸出十個數字、欄寬為4、靠左對齊）以及倍
數之個數、總和。
"""

a = eval(input())
b = eval(input())
newline=1
totalsum=0
for i in range(a,b+1):
    if (i%4==0 or i%9==0)and newline!=10:
        print('%-4d'%i,end='')
        newline+=1
        totalsum+=i
    elif i%4==0 or i%9==0:
        print('%-4d'%i)
        newline+=1
        totalsum+=i
print('\n%d'%(newline-1))    
print(totalsum)            