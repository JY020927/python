#3개의 주사위에서 같은 숫자가 나올 때까지 주사위를 던질 때, 던진 횟수와 각각의 주사위 눈을 출력하시오.(while 이용)

import random

throwCount = 0
while True:
    throwCount += 1
    a=random. randrange(1,7)
    b=random. randrange(1,7)
    c=random. randrange(1,7)

    print("(", a, b, c, ")")
    if a == b == c : #and/or/not
        print("주사위가 모두 동일한 숫자가 나옴 -->", a, b, c)
        break

print("3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 -->", throwCount)
