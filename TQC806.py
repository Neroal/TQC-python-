# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入一字串和一字元，
並將此字串及字元作為參數傳遞給名為compute()的函式，
此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。
"""

def compute(LIST,c):
    count=0
    for i in range(len(LIST)):
        if LIST[i] == c:
            count+=1
    return count

LIST = list(input())
c = input()
count=compute(LIST,c)
print(f'{c} occurs {count} time(s)')
    
