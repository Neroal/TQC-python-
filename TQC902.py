"""
請撰寫一程式，讀取read.txt的內容（內容為數字，
以空白分隔）並將這些數字加總後輸出。檔案讀取
完成後要關閉。
"""

infile = open('./database/read.txt','r')
total = 0

num = infile.read().split(' ')

for i in range(len(num)):
    total += int(num[i])

print(total)

infile.close()

