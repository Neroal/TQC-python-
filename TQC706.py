# -*- coding: utf-8 -*-
"""
全字母句（Pangram）是英文字母表所有的字母都出
現至少一次（最好只出現一次）的句子。請撰寫一
程式，要求使用者輸入一正整數k（代表有k筆測試
資料），每一筆測試資料為一句子，程式判斷該句
子是否為Pangram，並印出對應結果True（若是）或
False（若不是）。
"""

count= eval(input())

alpha=26

for i in range(count):
 sentence = input()
 set1 = set(sentence.lower())
 if ' ' in set1:
     set1.remove(' ')
 if len(set1) >= alpha:
     print('True')
 else:
     print('False')
 
 