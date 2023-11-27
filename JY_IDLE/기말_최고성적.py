#성적 5개를 리스트에 입력받아 최고 성적을 출력하시오.

scorces=[]

for i in range(5):
    scorces.append(int(input("성적을 입력하시오: ")))
print(scorces)

big = scorces[0]
for i in range(len(scorces)):
    if scorces[i] > big :
        big = scorces[i]

print("최고 점수 : ", big)
