#1부터 주어진 범위에서 배수의 개수를 출력하시오

c = int(input("숫자의 범위 n을 입력(1~n): "))
mul= int(input("구하려는 배수를 입력: "))
count= 0

for i in range(1, c):
    for i%mul == 0:
        count += 1
print("배수의 갯수: ", count)
