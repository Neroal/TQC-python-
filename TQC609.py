# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內
容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內
容以及它們相加的結果。
"""
user1 = []
user2 = []

print('Enter user 1:')
for i in range(2):
    user1.append([])
    for j in range(2):
        user1[i].append(eval(input()))
print('Enter user 2:')
for i in range(2):
    user2.append([])
    for j in range(2):
        user2[i].append(eval(input()))  
print('Matrix1:')
for i in range(2):
    for j in range(2):
        print(user1[i][j],end=' ')
    print() 
print('Matrix2:')      
for i in range(2):
    for j in range(2):
        print(user2[i][j],end=' ')
    print() 
print('Sum of 2 Matrix:') 
for i in range(2):
    for j in range(2):
        print(user2[i][j]+user1[i][j],end=' ')
    print() 
