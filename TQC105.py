"""
設計說明：
 請撰寫一程式，輸入兩個正數，代表一矩形之寬和
高，計算並輸出此矩形之高（Height）、寬（Width
）、周長（Perimeter）及面積（Area）。
 提示：輸出浮點數到小數點後第二位。
"""
height=eval(input(''))
width=eval(input(''))

print('Height = %.2f'%height)
print('Width = %.2f'%width)
print('Perimeter = %.2f'%(2*(height+width)))
print('Area = %.2f'%(height*width))