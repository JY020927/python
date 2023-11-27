#"hello" 문자열에서 입력한 문자가 있는지를 판단하도록 출력하시오. (if~in 구조 이용)

s =input('"hello" 에서 찾으려는 문자를 하나 입력하시오: ')
vowels = "hello"
find = False

for c in vowels:
    if s in c:
        print("%s" % s, "문자가 있음")
        find = True
        break
if find == False:
    print("%s" % s, "문자가 없음")
