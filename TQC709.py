
"""
請撰寫一程式，輸入一顏色詞典color_dict（以輸入
鍵值"end"作為輸入結束點，詞典中將不包含鍵值
"end"），再根據key值的字母由小到大排序並輸出
"""

color_dict = {}

while True:
    key = input('Key:')
    if key == 'end':
        break
    color_dict[key] = input('Value:')

for i in sorted(color_dict.keys()):
    print(i,': ',color_dict[i])
    

