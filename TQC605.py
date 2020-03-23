# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入十個成績，接下來將
十個成績中最小和最大值（最小、最大值不重複）
以外的成績作加總及平均，並輸出結果。
 提示：平均值輸出到小數點後第二位。
"""

size = 10
score = []
for i in range(size):
    score.append(eval(input()))
    
ans=sum(score)-max(score)-min(score)
print('%d'%ans)
print('%.2f'%(ans/8))