import turtle
t=turtle.Turtle()
t.shape('turtle')

s=input("도형을 입력하시오(사각형 또는 원 또는 삼각형):")
if s == "사각형" :
    w = int(input("가로: "))
    h = int(input("세로: "))

    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
elif s == "원" :
    r = int(input("원의 반지름: "))
    t.circle(r)
elif s =="삼각형" :
    b = int(input("삼각형의 변의 길이: "))
    
    t.forward(b)
    t.left(120)
    t.forward(b)
    t.left(120)
    t.forward(b)
else :
    print("잘못 입력했어요")
