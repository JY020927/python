#for문을 이용해서 팩토리얼을 계산한다. 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미함.
#n! = 1*2*3*......*(n-1)*n

fact = 1
n = int(input("정수를 입력하시오: "))

for i in range(1, n+1):
    fact = fact * i

print(n, "!은", "%d" % fact, "이다.")
