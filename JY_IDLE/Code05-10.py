import random

numbers = []
for num in range(0,10):       num은 제어변수(바꾸기 가능), in range는 함수(변경 불가)
    numbers.append(random.randrange(0,10))

print("생성된 리스트", numbers)

for num in range(0,10):
    if num not in numbers:
        print("숫자 %d는(은) 리스트에 없네요." %num)
