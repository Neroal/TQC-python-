# -*- coding: utf-8 -*-
"""
請使用選擇敘述撰寫一程式，根據使用者輸入的分
數顯示對應的等級。標準如下表所示：
 分 數 等 級
80 ~ 100 A
70 ~ 79 B
60 ~ 69 C
<= 59 F
"""
score = eval(input())

if 80<= score <= 100:
    print('A')
elif 70<= score <=79:
    print('B')
elif 60<= score <=69:
    print('C')
elif score<= 59:
    print('F')
else:
    print('genius!')
