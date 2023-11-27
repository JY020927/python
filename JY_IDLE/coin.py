import random
print("동전 던지기 게임을 시작합니다.(0: 앞, 1:뒤)")

#randrange(2) : 0-1 사이의 값을 리턴
coin = random.randrange(2)
if coin == 0 :
    print("난수 : %d , 앞면입니다." % coin)
else :
    print("난수 : %d , 뒷면입니다." % coin)
print("게임이 종료되었습니다.")
