# -*- coding: utf-8 -*-
"""
某次選舉有兩位候選人，分別是No.1: Nami、No.2:
Chopper。請撰寫一程式，輸入五張選票，輸入值如
為1即表示針對1號候選人投票；輸入值如為2即表示
針對2號候選人投票，如輸入其他值則視為廢票。每
次投完後需印出目前每位候選人的得票數，最後印
出最高票者為當選人；如最終計算有相同的最高票
數者或無法選出最高票者，顯示【=> No one won
the election.】。
"""

vote1 = vote2 = votenull = 0

for i in range(5):
    vote = eval(input())
    if vote == 1:
        vote1+=1        
    elif vote == 2:
        vote2+=1
    else:
        votenull+=1
    print('Total votes of NO.1:Nami = %d'%vote1)
    print('Total votes of NO.2:Chopper = %d'%vote2)
    print('Total null votes = %d'%votenull)

if vote1 > vote2:
    print('No.1 Nami won the election.')
elif vote2 < vote1:
    print('No.2 Chopper won the election.')
else:
     print('No one won the election.')