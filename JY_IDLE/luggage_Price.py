a=int(input("짐의 무게는 얼마입니까? "))

if a < 20 :
    print("짐에 대한 수수료는 없습니다. \n 감사합니다.")
else :
    price = (a - 20) * 2000
    print("수수료 : %d" % price)
    print("감사합니다.")
