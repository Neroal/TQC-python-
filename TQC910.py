# -*- coding: utf-8 -*-
"""
請撰寫一程式，要求使用者讀入read.dat（以UTF-8
編碼格式讀取），第一列為欄位名稱，第二列之後
是個人記錄。請輸出檔案內容並顯示男生人數和女
生人數（根據"性別"欄位，0為女性、1為男性）。
"""

file = open('./database/read.dat','r',encoding='UTF-8')
males = females = 0

for line in file:   
    print(line)
    line_split = line.split(' ')
    if line_split[2] == '1':
        males+=1
    elif line_split[2]=='0':
        females+=1
    
print(f'Number of males:{males}')
print(f'Number of females:{females}')

file.close()
