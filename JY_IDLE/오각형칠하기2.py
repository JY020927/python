#import random(오류)
from random import *
import turtle
t=turtle.Turtle()
t.shape('turtle')

t.fillcolor(random(), random(), random()) #r,g,b
t.begin_fill()
v =int(input("한변의 길이를 입력: "))

t.forward(v)
t.left(360/5)
t.forward(v)
t.left(360/5)
t.forward(v)
t.left(360/5)
t.forward(v)
t.left(360/5)
t.forward(v)
