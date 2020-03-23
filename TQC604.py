# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入十個整數作為樣本數
，輸出眾數（樣本中出現最多次的數字）及其出現
的次數
"""
size=10
num = []
count = [0]*size

for i in range(size):
    temp = eval(input())
    num.append(temp)
    count[num.index(temp)] += 1
maxcount = max(count)

print(num[count.index(maxcount)])
print(maxcount)
    

