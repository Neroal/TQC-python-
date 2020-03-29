# -*- coding: utf-8 -*-
"""
請撰寫一程式，要求使用者輸入一個密碼（字串）
，檢查此密碼是否符合規則。密碼規則如下：
a. 必須至少八個字元。
b. 只包含英文字母和數字。
c. 至少要有一個大寫英文字母。
d. 若符合上述三項規則，程式將顯示檢查結果為
【Valid password】，否則顯示【Invalid password】
"""
def lenCheck():
    global PASSWORD
    global FLAG
    if len(PASSWORD) >= 8:
        FLAG+=1
def charCheck():
    global PASSWORD
    global FLAG
    if PASSWORD.isalnum():
        FLAG+=1

def upperCheck():
    global PASSWORD
    global FLAG
    for i in range(len(PASSWORD)):
        if PASSWORD[i].isupper(): 
            FLAG+=1
            break
            
PASSWORD = input()
FLAG = 0

lenCheck()

charCheck()

upperCheck()

if FLAG ==3:
    print('Valid password')
else:
    print('Invalid password')

