#1부터 100사이의 모든 3의 배수의 합을 계산하여 출력하는 프로그램을 작성하시오. (while 이용)

sum = 0
number = 1

while number <=100:
    if number %3 == 0:
        sum = sum + number
    number = number + 1
print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다." % sum)
