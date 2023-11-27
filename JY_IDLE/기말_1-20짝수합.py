#1~20 사이의 짝수의 합을 구하기
# (% 나머지 연산자 이용 --> if문)

i, hap = 0, 0

for i in range(0, 21, 1):
    if i%2 == 0 :
        hap = hap + i

print("1부터 20 사이의 짝수의 합을 구하시오: %d" % hap)
