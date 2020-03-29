"""
請撰寫一程式，為一詞典輸入資料（以輸入鍵值
"end"作為輸入結束點，詞典中將不包含鍵值"end"）
，再輸入一鍵值並檢視此鍵值是否存在於該詞典中。
"""

data_dist = {}

while True:
    key = input('Key:')
    
    if key == 'end':
        break
    data_dist[key] = input('Value:')
    
search = input('Search key:')

print(search in data_dist.keys())


