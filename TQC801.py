# -*- coding: utf-8 -*-
"""
請撰寫一程式，要求使用者輸入一字串，顯示該字
串每個字元的索引。
"""

LIST = input()

for i in range(len(LIST)):
    print("Index of '%s':"%LIST[i],i)