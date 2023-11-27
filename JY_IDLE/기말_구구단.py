#입력받은 숫자의 구구단을 출력하시오. (while 이용)

num=int(input("출력할 구구단을 입력 : "))

i=1
while i <= 9:
    print("%d*%d = %d" % (num, i, num*i))
    i = i + 1
