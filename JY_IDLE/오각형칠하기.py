import turtle
t=turtle.Turtle()
t.shape('turtle')

t.pencolor("violet")
t.fillcolor("pink")
t.begin_fill()
v=int(input("한변의 길이를 입력: "))

t.forward(v)
t.left(360/5)
t.forward(v)
t.left(360/5)
t.forward(v)
t.left(360/5)
t.forward(v)
t.left(360/5)
t.forward(v)
