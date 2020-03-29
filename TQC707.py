"""
請撰寫一程式，輸入X組和Y組各自的科目至集合中
，以字串"end"作為結束點（集合中不包含字串"end"
）。請依序分行顯示(1) X組和Y組的所有科目、
(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科
目，以及(4) X組和Y組彼此沒有的科目（不包含相
同科目）。
 提示：科目須參考範例輸出樣本，依字母由小至大
進行排序。
"""
xS = set()
yS = set()

print('Enter group X subject:')

x = input()

while x != 'end':
    xS.add(x)
    x=input()
    
print('Enter group Y subject:')
y = input()

while y != 'end':
    yS.add(y)
    y=input()
    
print(sorted(xS.union(yS)))
print(sorted(yS.intersection(xS)))
print(sorted(yS.difference(xS)))
print(sorted(yS.symmetric_difference(xS)))



