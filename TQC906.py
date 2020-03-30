"""
請撰寫一程式，要求使用者輸入檔名data.txt、字串
s1和字串s2。程式將檔案中的字串s1以s2取代之。
"""
filename = input()
s1 = input()
s2 = input()

file = open('./database/'+filename,'r+',encoding='UTF-8')
data = file.read()

print('=== Before the replacement ===')
print(data)

print('=== After the replacement ===')
data = data.replace(s1,s2)
print(data)

file.seek(0,0)
file.truncate()
file.write(data)
file.close()


