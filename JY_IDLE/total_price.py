a=int(input("구입 금액을 입력하시오: "))
discount=0
if a >=100000 :
    discount = a * 0.05
    sales = a-discount
else :
    sales = a

print("할인금액: %d원 , 지불 금액은 %d원") <-??
