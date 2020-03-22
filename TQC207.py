# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，要求使用者輸入購物
金額，購物金額需大於8,000（含）以上，並顯示折
扣優惠後的實付金額。購物金額折扣方案如下表所
示：
 金 額 折 扣
8,000（含） 以上9.5折
18,000（含） 以上9折
28,000（含） 以上8折
38,000（含） 以上7折
"""

cash = eval(input())

if cash >=38000:
    print(cash*0.7)
elif cash >=28000:
    print(cash*0.8)
elif cash >=18000:
    print(cash*0.9)
elif cash >=8000:
    print(cash*0.95)
else:
    print(cash)