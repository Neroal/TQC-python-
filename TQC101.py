'''
請撰寫一程式，輸入四個整數，然後將這四個整數
以欄寬為5、欄與欄間隔一個空白字元，再以每列印
兩個的方式，先列印向右靠齊，再列印向左靠齊，
左右皆以直線 |（Vertical bar）作為邊界。 
'''
number1 = int(input(''))
number2 = int(input(''))
number3 = int(input(''))
number4 = int(input(''))

print('|%5d %5d|'%(number1,number2))
print('|%5d %5d|'%(number3,number4))
print('|%-5d %-5d|'%(number1,number2))
print('|%-5d %-5d|'%(number3,number4))

