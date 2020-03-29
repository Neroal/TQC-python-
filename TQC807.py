# -*- coding: utf-8 -*-
"""
請撰寫一程式，要求使用者輸入一字串，該字串為
五個數字，以空白隔開。請將此五個數字加總（
Total）並計算平均（Average）。
"""

LIST = list(input().split(' '))
total=0
for i in range(len(LIST)):
    total += int(LIST[i])
avg = total/5    
print(f'Total = {total}')
print(f'Average = {avg}')

