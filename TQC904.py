"""
請撰寫一程式，讀取read.txt（每一列的格式為名字
和身高、體重，以空白分隔）並顯示檔案內容、所
有人的平均身高、平均體重以及最高者、最重者。
"""

infile = open('./database/read904.txt','r')

name ,height ,weight = [],[],[]

line = infile.readline()

while line != '':
    print(line)
    data = line.split()
    name.append(data[0])
    height.append(int(data[1]))
    weight.append(int(data[2]))
    line = infile.readline()

print('Average Height: %.2f'%(sum(height)/len(height)))
print('Average Weight: %.2f'%((sum(weight)/len(weight))))

print('The tallest is %s with %.2f cm'%(name[height.index(max(height))],max(height)))
print('The heaviest is %s with %.2f kg'%(name[weight.index(max(weight))],max(weight)))
infile.close()




