# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個正
整數，然後判斷它是3或5的倍數，顯示【x is a
multiple of 3.】或【x is a multiple of 5.】；若此數值
同時為3與5的倍數，顯示【x is a multiple of 3 and 5.
】；如此數值皆不屬於3或5的倍數，顯示【x is not a
multiple of 3 or 5.】，將使用者輸入的數值代入x。
"""
x = eval(input(''))

if x%3==0 and x%5==0:
    print('%d is a multiple of 3 and 5.'%x)
elif x%3==0:
    print('%d is a multiple of 3.'%x)
elif x%5==0:
    print('%d is a multiple of 5.'%x)
else:
    print('%d is not a multiple of 3 or 5.'%x)
