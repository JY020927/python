#while을 이용하여 숫자를 리스트에 입력하여 합을 구하시오

aa = [0, 0, 0, 0]
hap = 0

i=0
while (i < 4):
    aa[i] = int(input("%d번째 숫자 : " %(i+1)))
    hap = hap + aa[i]
    i = i + 1

print("합계 ==> %d" % hap)
