# -*- coding: utf-8 -*-
"""
請使用迴圈敘述撰寫一程式，讓使用者輸入正整數n
(1 < n)，計算以下公式的總和並顯示結果：
 提示：輸出結果至小數點後四位。
"""

n = eval(input())
ans=0

for i in range(1,n):
    ans+=(1/(pow(i,0.5)+pow(i+1,0.5)))

print('%.4f'%ans)    
