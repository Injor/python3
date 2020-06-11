
#PythonDraw.py
import turtle
#宽度，高度，左上角的x，y
turtle.setup(650,350,200,200)
#起笔
turtle.penup()
#正前方向，forword
turtle.fd(-250)
#落笔
turtle.pendown()
#笔迹宽度
turtle.pensize(25)
#颜色
turtle.pencolor("purple")
#改变行进方向
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
#画圆，半径，弧度
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
#不自动退出，需手动结束
turtle.done()
