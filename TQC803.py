# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入一個句子（至少有五
個詞，以空白隔開），並輸出該句子倒數三個詞。
"""

s = input().split(' ')

for i in range(-3,0):
    print(s[i],end=' ')


