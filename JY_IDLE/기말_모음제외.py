#문자열을 입력받아서 모음을 제외한 문자열을 출력하시오. (대소문자 모두 포함하여 제외)

s = input("문자열을 입력하시오: ")
vowels = "aeiouAEIOU"
result = ""
for letter in s:
    if letter not in vowels:
        result += letter
    print(result)
