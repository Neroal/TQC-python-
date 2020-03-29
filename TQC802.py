# -*- coding: utf-8 -*-
"""
請撰寫一程式，要求使用者輸入一字串，顯示該字
串每個字元的對應ASCII碼及其總和。
"""

string = input()
total = 0
for i in range(len(string)):
    total += ord(string[i])
    print("ASCII code for '%s' is %d"%(string[i],ord(string[i])))
print(total)

