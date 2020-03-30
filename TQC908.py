"""
請撰寫一程式，要求使用者輸入檔名read.txt，以及
檔案中某單字出現的次數。輸出符合次數的單字，
並依單字的第一個字母大小排序。（單字的判斷以
空白隔開即可）
"""

word_dict = dict()
filename = input()

file = open('./database/'+filename,'r',encoding = 'UTF-8')

count = eval(input())

for line in file:
    line_split = line.split(' ')
    for word in line_split:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word] = 1

for word in sorted(word_dict):
    if word_dict[word] == count:
        print(word)
