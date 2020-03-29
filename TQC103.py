'''
設計說明：
 請撰寫一程式，輸入四個單字，然後將這四個單字
以欄寬為10、欄與欄間隔一個空白字元、每列印兩
個的方式，先列印向右靠齊，再列印向左靠齊，左
右皆以直線 |（Vertical bar）作為邊界。
'''
a = str(input())
b = str(input())
c = str(input())
d = str(input())

print('|%10s %10s|'%(a,b))
print('|%10s %10s|'%(c,d))
print('|%-10s %-10s|'%(a,b))
print('|%-10s %-10s|'%(c,d))