Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #공백, 영문자, 숫자인지를 판단
>>> isspace(), isalpha(), isdigit()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    isspace(), isalpha(), isdigit()
NameError: name 'isspace' is not defined
>>> "a".isalpha()
True
>>> "3".isalpha()
False
>>> "a3".isalpha()
False
>>> "aa".isalpha()
True
>>> "3".isdight()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    "3".isdight()
AttributeError: 'str' object has no attribute 'isdight'
>>> "3".isdigit()
True
>>> "3a".isdigit()
False
>>> " ".isspace()
True
>>> "  3".isspace()
False
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_개수출력.py ============
문장을 입력하시오: hello nice to meet you 33
알파벳 문자의 개수=  18
숫자 문자의 개수=  2
스페이스 문자의 개수=  5
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_평균구하기.py ============
전체 학생수는 : 3
과목수 : 4
1번 학생의 과목1 점수 : 90
1번 학생의 과목2 점수 : 78
1번 학생의 과목3 점수 : 85
1번 학생의 과목4 점수 : 77
1번 학생의 성적 평균 : 82.5
2번 학생의 과목1 점수 : 34
2번 학생의 과목2 점수 : 67
2번 학생의 과목3 점수 : 84
2번 학생의 과목4 점수 : 90
2번 학생의 성적 평균 : 68.8
3번 학생의 과목1 점수 : 12
3번 학생의 과목2 점수 : 21
3번 학생의 과목3 점수 : 34
3번 학생의 과목4 점수 : 99
3번 학생의 성적 평균 : 41.5
>>> i=0
>>> while i < 3:
	print("%d : 안녕하세요? while문을 공부 중입니다. ^^" % i)
	i = i + 1

	
0 : 안녕하세요? while문을 공부 중입니다. ^^
1 : 안녕하세요? while문을 공부 중입니다. ^^
2 : 안녕하세요? while문을 공부 중입니다. ^^
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-09.py ===========
1에서 10까지의 합계 : 55
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_구구단.py =============
출력할 구구단을 입력 : 9
9*1 = 9
9*2 = 18
9*3 = 27
9*4 = 36
9*5 = 45
9*6 = 54
9*7 = 63
9*8 = 72
9*9 = 81
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_3배수 합.py ============
1부터 100 사이의 모든 3의 배수의 합은 1683입니다.
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_자리수합.py ============
정수를 입력하시오 : 2345
자리수의 합:  14
>>> while True :
	print("ㅋ", end = " ")

	
ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    print("ㅋ", end = " ")
KeyboardInterrupt
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-10.py ===========
더할 첫 번째 수를 입력하세요 : 55
더할 두 번째 수를 입력하세요 : 22
55 + 22 = 77
더할 첫 번째 수를 입력하세요 : 77
더할 두 번째 수를 입력하세요 : 128
77 + 128 = 205
더할 첫 번째 수를 입력하세요 : 11
더할 두 번째 수를 입력하세요 : 22
11 + 22 = 33
더할 첫 번째 수를 입력하세요 : 3
더할 두 번째 수를 입력하세요 : 4
3 + 4 = 7
더할 첫 번째 수를 입력하세요 : 555555
더할 두 번째 수를 입력하세요 : 666666
555555 + 666666 = 1222221
더할 첫 번째 수를 입력하세요 : 1212121212
더할 두 번째 수를 입력하세요 : 1212121212
1212121212 + 1212121212 = 2424242424
더할 첫 번째 수를 입력하세요 : 
Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/Code06-10.py", line 5, in <module>
    a= int(input("더할 첫 번째 수를 입력하세요 : "))
KeyboardInterrupt
>>> import random
>>> 
>>> random. randrange(1,7)
5
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 5 2 4 )
( 6 5 5 )
( 6 4 1 )
( 1 1 6 )
( 5 3 1 )
( 4 3 5 )
( 5 1 4 )
( 6 1 2 )
( 3 4 3 )
( 4 5 5 )
( 5 4 6 )
( 1 2 5 )
( 2 2 1 )
( 1 1 1 )
주사위가 모두 동일한 숫자가 나옴 --> 1 1 1
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 14
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 5 2 5 )
( 2 2 4 )
( 3 2 4 )
( 2 1 4 )
( 5 5 1 )
( 6 6 5 )
( 6 2 6 )
( 6 3 6 )
( 1 2 5 )
( 6 3 5 )
( 5 6 4 )
( 6 6 2 )
( 6 5 2 )
( 1 4 3 )
( 6 4 5 )
( 2 3 5 )
( 5 4 3 )
( 2 4 4 )
( 6 4 4 )
( 3 6 1 )
( 5 5 2 )
( 2 6 2 )
( 6 4 2 )
( 4 2 3 )
( 2 4 2 )
( 5 6 6 )
( 6 3 5 )
( 4 1 5 )
( 4 4 4 )
주사위가 모두 동일한 숫자가 나옴 --> 4 4 4
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 29
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 5 3 3 )
( 2 1 6 )
( 6 4 2 )
( 5 4 2 )
( 1 3 6 )
( 6 5 1 )
( 6 2 1 )
( 4 2 6 )
( 6 4 4 )
( 2 5 2 )
( 2 1 6 )
( 2 1 3 )
( 1 1 6 )
( 2 6 4 )
( 6 6 6 )
주사위가 모두 동일한 숫자가 나옴 --> 6 6 6
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 15
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 2 2 1 )
( 3 3 6 )
( 6 2 2 )
( 6 1 5 )
( 5 3 6 )
( 1 4 6 )
( 4 3 1 )
( 1 5 4 )
( 5 1 6 )
( 3 2 6 )
( 5 2 5 )
( 5 6 5 )
( 5 6 4 )
( 2 6 5 )
( 6 3 5 )
( 3 1 3 )
( 5 6 4 )
( 5 3 4 )
( 5 5 1 )
( 5 2 5 )
( 1 5 5 )
( 1 4 4 )
( 6 6 6 )
주사위가 모두 동일한 숫자가 나옴 --> 6 6 6
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 23
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 2 5 3 )
( 1 4 1 )
( 6 2 1 )
( 2 6 1 )
( 6 1 6 )
( 3 2 4 )
( 4 1 5 )
( 5 3 4 )
( 4 4 4 )
주사위가 모두 동일한 숫자가 나옴 --> 4 4 4
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 9
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 2 4 5 )
( 5 5 4 )
( 3 1 2 )
( 4 6 2 )
( 1 2 6 )
( 6 3 6 )
( 4 2 3 )
( 1 3 5 )
( 6 5 1 )
( 3 2 3 )
( 3 3 6 )
( 3 6 3 )
( 3 1 2 )
( 6 3 4 )
( 4 2 2 )
( 4 5 5 )
( 2 1 2 )
( 3 4 2 )
( 2 6 3 )
( 4 5 6 )
( 4 5 6 )
( 3 3 3 )
주사위가 모두 동일한 숫자가 나옴 --> 3 3 3
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 22
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 6 2 4 )
( 1 4 2 )
( 3 1 6 )
( 2 6 4 )
( 3 5 1 )
( 6 3 1 )
( 5 5 1 )
( 3 4 4 )
( 1 3 1 )
( 4 4 5 )
( 3 3 5 )
( 1 5 3 )
( 6 5 4 )
( 1 3 6 )
( 3 4 4 )
( 3 4 4 )
( 1 3 2 )
( 2 4 5 )
( 6 5 2 )
( 2 1 2 )
( 5 3 3 )
( 1 4 3 )
( 1 2 2 )
( 1 3 5 )
( 2 4 2 )
( 6 6 6 )
주사위가 모두 동일한 숫자가 나옴 --> 6 6 6
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 26
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 2 2 1 )
( 2 3 6 )
( 4 6 1 )
( 4 1 6 )
( 6 5 1 )
( 6 4 1 )
( 4 6 5 )
( 1 4 6 )
( 1 6 1 )
( 1 2 3 )
( 1 5 6 )
( 3 5 3 )
( 3 4 5 )
( 6 5 3 )
( 6 4 4 )
( 1 5 5 )
( 2 6 4 )
( 5 5 3 )
( 2 2 4 )
( 4 3 2 )
( 1 1 4 )
( 4 1 5 )
( 3 1 2 )
( 3 6 1 )
( 4 3 6 )
( 6 6 6 )
주사위가 모두 동일한 숫자가 나옴 --> 6 6 6
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 26
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 1 5 6 )
( 4 6 1 )
( 1 6 2 )
( 2 4 4 )
( 1 5 2 )
( 4 4 4 )
주사위가 모두 동일한 숫자가 나옴 --> 4 4 4
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 6
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 4 4 1 )
( 1 6 3 )
( 6 2 6 )
( 3 4 2 )
( 4 2 2 )
( 3 6 4 )
( 2 1 2 )
( 2 4 3 )
( 6 5 4 )
( 1 2 5 )
( 4 1 3 )
( 1 6 5 )
( 6 6 6 )
주사위가 모두 동일한 숫자가 나옴 --> 6 6 6
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 13
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_주사위.py =============
( 2 6 3 )
( 6 2 3 )
( 1 6 4 )
( 4 3 1 )
( 3 5 4 )
( 4 2 5 )
( 5 1 4 )
( 3 6 4 )
( 5 2 4 )
( 5 3 2 )
( 4 5 3 )
( 2 3 4 )
( 1 1 4 )
( 1 1 5 )
( 4 1 1 )
( 1 4 4 )
( 4 3 6 )
( 4 2 4 )
( 3 3 1 )
( 4 4 1 )
( 2 6 1 )
( 6 2 3 )
( 3 2 4 )
( 4 2 2 )
( 6 6 2 )
( 1 5 4 )
( 6 2 6 )
( 6 6 3 )
( 6 3 6 )
( 5 6 1 )
( 2 3 1 )
( 2 4 2 )
( 1 6 3 )
( 4 5 6 )
( 6 5 2 )
( 3 4 5 )
( 1 5 1 )
( 5 6 2 )
( 2 6 3 )
( 6 4 3 )
( 6 3 5 )
( 5 6 3 )
( 1 5 4 )
( 5 6 2 )
( 4 4 2 )
( 5 2 2 )
( 1 1 1 )
주사위가 모두 동일한 숫자가 나옴 --> 1 1 1
3개가 동일한 숫ㅈ가 나올 때까지 주사위를 던진 횟수 --> 47
>>> 