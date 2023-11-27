#문장을 입력받아 알파벳 문자의 갯수, 숫자의 개수, 스페이스의 개수를 출력하는 프로그램을 작성하시오.

statement=input("문장을 입력하시오: ")

alphas = 0
digits = 0
spaces = 0

for c in statement:
    if c.isalpha():
        alphas = alphas + 1
    if c.isdigit():
        digits = digits + 1
    if c.isspace():
        spaces = spaces + 1

print("알파벳 문자의 개수= ", alphas)
print("숫자 문자의 개수= ", digits)
print("스페이스 문자의 개수= ", spaces)
