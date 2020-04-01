# -*- coding: utf-8 -*-
"""
請使用迴圈敘述撰寫一程式，提示使用者輸入金額
（如10,000）、年收益率（如5.75），以及經過的月
份數（如5），接著顯示每個月的存款總額。
 提示：四捨五入，輸出浮點數到小數點後第二位
"""

amount = eval(input())
rate = eval(input())
period = eval(input())

#change to percent
rate/=100

print('%s\t%s'%('Month','Amount'))
for month in range(1,period+1):
    total = amount + (amount*(rate/12))
    print('%d\t%.2f'%(month,total))
    amount = total
    
