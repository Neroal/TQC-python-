# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入52張牌中的5張，計算
並輸出其總和。
"""
size=5
ans=0
card=[]
for i in range(size):
    card.append(input())
    if card[i] == 'a' or card[i] == 'A':
        ans+=1
    elif card[i] == 'j' or card[i] =='J':
        ans+=11
    elif card[i] == 'q' or card[i]=='Q':
        ans+=12
    elif card[i] == 'k' or card[i]=='K':
        ans+=13
    elif card[i] == '10':
        ans+=10
    else:
        ans += eval(card[i])
print(ans)