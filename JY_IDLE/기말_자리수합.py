#정수를 입력하면 각 자리수의 합을 구하는 프로그램을 작성하시오.(while, % 와 //를 이용)

number = int(input("정수를 입력하시오 : "))

sum = 0

while number != 0:
    sum = sum + number % 10
    number = number // 10

print("자리수의 합: " , sum)
