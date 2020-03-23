# -*- coding: utf-8 -*-
"""
請撰寫一程式，輸入一些字串至數組（至少輸入五
個字串），以字串"end"為結束點（數組中不包含字
串"end"）。接著輸出該數組，再分別顯示該數組的
第一個元素到第三個元素和倒數三個元素。
"""

TUPLE = ()
string = input()
while string != "end":
    TUPLE +=(string,)
    string = input()
print(TUPLE)
print(TUPLE[0:3])
print(TUPLE[-3:])
