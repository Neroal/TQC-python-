"""
設計說明：
 假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫
一程式，輸入x、y、z數值，最後顯示此選手每小時
的平均英哩速度（1英哩等於1.6公里）。
 提示：輸出浮點數到小數點後第一位。
"""
x = eval(input())
y = eval(input())
z = eval(input())

speed = (z/1.6)/((x*60+y)/3600)

print('Speed = %.1f'%speed)
