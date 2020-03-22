# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個字
元，判斷它是包括大、小寫的英文字母（alphabet）
、數字（number）、或者其它字元（symbol）。例
如：a為英文字母、9為數字、$為其它字元。
"""

char = input()

if ('a' <= char <= 'z') or ('A' < char < 'Z'):
    print('%c is an alphabet.'%char)
elif ('0' <= char <= '9'):
    print('%c is an number.'%char)
else:
    print('%c is an symble.'%char)


