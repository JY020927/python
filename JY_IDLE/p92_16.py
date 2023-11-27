num=input("글자 입력: ")
if ('0' <= num and num <= '1') :
    print("2진수 또는 8진수 또는 16진수 입니다")
elif ('2' <= num and num <= '7') :
    print("8진수 또는 10진수 또는 16진수 입니다")
elif ('8' <= num and num <= '9') :
    print("10진수 또는 16진수 입니다")
elif ('a' <= num and num <= 'f') or ('A' <= num and num <= 'F') :
    print("16진수 입니다.")
else :
    print("숫자가 아닙니다")
