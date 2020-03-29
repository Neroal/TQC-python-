# -*- coding: utf-8 -*-
"""
請撰寫一程式，提示使用者輸入一個社會安全碼
SSN，格式為ddd-dd-dddd，d表示數字。若格式完全
符合（正確的SSN）則顯示【Valid SSN】，否則顯
示【Invalid SSN】。
"""

SSN = list(input().split('-'))
FLAG = True
for i in range(len(SSN)):
    if not SSN[i].isdigit():
        print('Invalid SSN')
        FLAG = False
if FLAG == True:
    print('Valid SSN')