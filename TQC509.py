# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入二個分數，分別是x/y
和m/n（其中x、y、m、n皆為正整數），計算這兩
個分數的和為p/q，接著將p和q傳遞給名為compute()
函式，此函式回傳p和q的最大公因數（Greatest
Common Divisor, GCD）。再將p和q各除以其最大公
因數，最後輸出的結果必須以最簡分數表示。
"""
def  compute(x,y):
    gcd = 1  
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd  

x,y = eval(input())
m,n = eval(input())
q = y*n
p = m*y+x*n
gcd=compute(p,q)

print(x,'/',y,' + ',m,'/',n,' = ',int(p/gcd),'/',int(q/gcd))

