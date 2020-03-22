# -*- coding: utf-8 -*-
"""
請撰寫一程式，呼叫函式compute()，該函式功能為
讓使用者輸入系別（Department）、學號（Student
ID）和姓名（Name）並顯示這些訊息。
"""

def compute():
    department = eval(input())
    studentid = eval(input())
    name = eval(input())
    print('Department:',department)
    print('Student ID:',studentid)
    print('Name:',name)

compute()
