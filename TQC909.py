"""
請撰寫一程式，將使用者輸入的五個人的資料寫入
data.dat檔，每一個人的資料為姓名和電話號碼，以
空白分隔。再將檔案加以讀取並顯示檔案內容。
"""

file = open('./database/data.dat','w+',encoding='UTF-8')

for i in range(5):
    file.write(input()+'\n')

print('Content of "data.dat"')
file.seek(0,0)

print(file.read())
    
file.close()


