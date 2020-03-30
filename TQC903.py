# -*- coding: utf-8 -*-
"""
請撰寫一程式，要求使用者輸入五個人的名字並加
入到data.txt的尾端。之後再顯示此檔案的內容。
"""

outfile = open('./database/data.txt','a+')

for i in range(5):
    outfile.write('\n'+input())
    
print('Append completed!')
print('Content of "data.txt"')

outfile.seek(0,0)
print(outfile.read())

outfile.close()

