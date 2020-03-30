"""
請撰寫一程式，要求使用者輸入檔案名稱data.txt和
一字串s，顯示該檔案的內容。接著刪除檔案中的字
串s，顯示刪除後的檔案內容並存檔。
"""

filename = input()
food = input()
file = open(('./database/'+filename),'r+',encoding='UTF-8')
print('===Before the deletion===')

line = file.read()
print(line)

print('===After the deletion===')
line = line.replace(food,'')
print(line)

file.seek(0,0)
file.truncate()
file.write(line)

file.close()


