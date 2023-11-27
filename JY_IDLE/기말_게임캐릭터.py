#게임 캐릭터 3개를 입력받아 list에 저장 후, 출력하시오. (for문 사용)

aa=[]

for i in range(0, 3):
    str = input("좋아하는 게임 캐릭터 : ")
    aa.append(str)

print(aa)
