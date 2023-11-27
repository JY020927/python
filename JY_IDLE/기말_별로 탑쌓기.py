#숫자를 입력받아서 별을 출력하시오.

count = int(input("출력할 라인의 수: "))

for i in range(count):
    for j in range(i+1):
        print("*", end="")
    print("")
