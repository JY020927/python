Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Users/AISASE/Documents/JY_IDLE/month.py =============
월을 입력하시오: 1
월의 날수는 31일
>>> 
============== RESTART: C:/Users/AISASE/Documents/JY_IDLE/month.py =============
월을 입력하시오: 2
월의 날수는 29일
>>> 
============== RESTART: C:/Users/AISASE/Documents/JY_IDLE/month.py =============
월을 입력하시오: 6
월의 날수는 30일
>>> 
============ RESTART: C:\Users\AISASE\Documents\JY_IDLE\Code05-08.py ===========
점수를 입력하세요 : 55
F
학점입니다. ^^
>>> 
============ RESTART: C:\Users\AISASE\Documents\JY_IDLE\Code05-08.py ===========
점수를 입력하세요 : 66
D+
학점입니다. ^^
>>> 
============ RESTART: C:\Users\AISASE\Documents\JY_IDLE\Code05-08.py ===========
점수를 입력하세요 : 97
A+
학점입니다. ^^
>>> import random
>>> random.randrange(2)
1
>>> random.randrange(2)
1
>>> random.randrange(2)
1
>>> random.randrange(2)
0
>>> random.randrange(2)
0
>>> random.randrange(2) "0<=?<2"
SyntaxError: invalid syntax
>>> random.randrange(2)
1
>>> random.randrange(2)
0
>>> 
============== RESTART: C:/Users/AISASE/Documents/JY_IDLE/coin.py ==============
동전 던지기 게임을 시작합니다.(0: 앞, 1:뒤)
Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/coin.py", line 1, in <module>
    coin=int(input("동전 던지기 게임을 시작합니다.(0: 앞, 1:뒤)"))
ValueError: invalid literal for int() with base 10: ''
>>> 
============== RESTART: C:/Users/AISASE/Documents/JY_IDLE/coin.py ==============
동전 던지기 게임을 시작합니다.(0: 앞, 1:뒤)
난수 : 1 , 뒷면입니다.
게임이 종료되었습니다.
>>> 
============== RESTART: C:/Users/AISASE/Documents/JY_IDLE/coin.py ==============
동전 던지기 게임을 시작합니다.(0: 앞, 1:뒤)
난수 : 0 , 앞면입니다.
게임이 종료되었습니다.
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/lottoTest.py ===========
생성된 로또숫자: %d
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/lottoTest.py ===========
생성된 로또숫자: 
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/lottoTest.py ===========
생성된 로또숫자: 8
>>> jumsu = 55
>>> res = ' '
>>> if jumsu >= 60 :
	res = ' 합격'
	else :
		
SyntaxError: invalid syntax
>>> res = '합격' if jumsu >= 60 else '불합격'
>>> 
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/samhang.py ============
불합격
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/samhang.py ============
불합격
>>> fruit = ['사과', '배', '딸기', '포도']
>>> print(fruit)
['사과', '배', '딸기', '포도']
>>> fruit.append('귤')
>>> print(fruit)
['사과', '배', '딸기', '포도', '귤']
>>> if '딸기' in fruit :
print("딸기가 있네요. ^^")
SyntaxError: expected an indented block
>>>  fruit.append('50')
 
SyntaxError: unexpected indent
>>> >>> fruit = ['사과', '배', '딸기', '포도']
>>> print(fruit)
['사과', '배', '딸기', '포도']
>>> fruit.append('귤')
>>> print(fruit)
['사과', '배', '딸기', '포도', '귤']
SyntaxError: invalid syntax
>>> fruit = ['사과', '배', '딸기', '포도']
>>> print(fruit)
['사과', '배', '딸기', '포도']
>>> fruit.append('귤')
>>> print(fruit)
['사과', '배', '딸기', '포도', '귤']
>>> if '딸기' in fruit:
	print("딸기가 있어요. ^^")

	
딸기가 있어요. ^^
>>> for i in range(0,3,1) :
	print("안녕하세요? for 문을 공부 중입니다. ^^")

	
안녕하세요? for 문을 공부 중입니다. ^^
안녕하세요? for 문을 공부 중입니다. ^^
안녕하세요? for 문을 공부 중입니다. ^^
>>> for _ in range(3):
	print("hello")

	
hello
hello
hello
>>> for i in range(0, 3, 1) :
	print("%d : 안녕하세요? for 문을 공부 중입니다. ^^" %i)

	
0 : 안녕하세요? for 문을 공부 중입니다. ^^
1 : 안녕하세요? for 문을 공부 중입니다. ^^
2 : 안녕하세요? for 문을 공부 중입니다. ^^
>>> for i in range(2,-1,-1) :
	print("%d : 안녕하세요? for 문을 공부 중입니다.")

	
%d : 안녕하세요? for 문을 공부 중입니다.
%d : 안녕하세요? for 문을 공부 중입니다.
%d : 안녕하세요? for 문을 공부 중입니다.
>>> for i in range(2,-1,-1) :
	print("%d : 안녕하세요? for 문을 공부 중입니다. ^^" % i)

	
2 : 안녕하세요? for 문을 공부 중입니다. ^^
1 : 안녕하세요? for 문을 공부 중입니다. ^^
0 : 안녕하세요? for 문을 공부 중입니다. ^^
>>> for i in range(1,6,1):
	print("%d " %i, end = " ")

	
1  2  3  4  5  
>>> 
>>> for i in range(1,6,1):
	print("%d " %i)

	
1 
2 
3 
4 
5 
>>> 