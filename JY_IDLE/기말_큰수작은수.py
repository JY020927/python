#숫자의 개수를 입력받은 후, 제일 큰 숫자와 제일 작은 수를 구하시오. (while 이용)

num = int(input("입력할 숫자의 갯수 : "))
i = 0

su = int(input("숫자를 입력: "))
max = min = su
while  (i < num-1):
    su = int(input("숫자를 입력 : "))
    if max < su :
        max = su
    if min > su :
        min = su
    i = i + 1

print("최대값 : %d, 최소값 : %d" % (max, min))
