"""
設計說明：
 請撰寫一程式，讓使用者輸入五個數字，計算並輸
出這五個數字之數值、總和及平均數。
 提示：輸出浮點數到小數點後第1位。
"""
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
num5 = eval(input())

summ = num1+num2+num3+num4+num5
avg = summ/5
print(num1,num2,num3,num4,num5)
print('Sum = %.1f'%summ)
print('Average = %.1f'%avg)


