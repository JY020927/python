appleQuality=input("사과의 상태를 입력하시오(ex. 신선 or 보통): ")
applePrice=int(input("사과 1개의 가격을 입력하시오: "))
price = 0
if appleQuality == "신선":
    if applePrice < 1000 :
        price = 10 * applePrice
    else :
        price = 5 * applePrice
else:
    pass
    #price = 0

print("총 가격: ", price)
