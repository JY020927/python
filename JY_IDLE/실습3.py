Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> money, c50000, c10000, c5000, c1000 = 0, 0, 0, 0, 0
>>> 
>>> money=int(input("교환할 돈은 얼마?"))
교환할 돈은 얼마?
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    money=int(input("교환할 돈은 얼마?"))
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: C:/Users/AISASE/Documents/JY_IDLE/selfstudy_4-1.py =========
교환할 돈은 얼마?777777

 50000원짜리 ==> 15개

 10000원짜리 ==> 2개

 5000원짜리 ==> 1개

 1000원짜리 ==> 2개
 지폐로 바꾸지 못한 돈 ==> 777원

>>> 
========== RESTART: C:/Users/AISASE/Documents/JY_IDLE/selfstudy_4-1.py =========
교환할 돈은 얼마?777777
Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/selfstudy_4-1.py", line 17, in <module>
    print("\n 50000원짜리 ==> %장" % c50000)
ValueError: unsupported format character '?' (0xc7a5) at index 16
>>> 
========== RESTART: C:/Users/AISASE/Documents/JY_IDLE/selfstudy_4-1.py =========
교환할 돈은 얼마?777777

 50000원짜리 ==> 15장

 10000원짜리 ==> 2장

 5000원짜리 ==> 1장

 1000원짜리 ==> 2장
 지폐로 바꾸지 못한 돈 ==> 777원

>>> print('%d / %d = %d' % (5, 10, 5/10))
5 / 10 = 0
>>> print("%04d"%876)
0876
>>> print("%5s"%"Cookbook")
Cookbook
>>> print("%1.1f"%123.45)
123.5
>>> print("{2:d} {0:d} {1:d}".format(111, 222, 333))
333 111 222
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/vending.py ============
투입한 돈: 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/vending.py ============
투입한 돈: 1000
물건값: 200
거스름돈:  800

 500원 동전의 개수: 2
 100원 동전의 개수: 0
>>> 
============= RESTART: C:/Users/AISASE/Documents/JY_IDLE/vending.py ============
투입한 돈: 1000
물건값: 200
거스름돈:  800
 500원 동전의 개수:  1
100원 동전의 개수:  3
>>> a=99
>>> if a < 100 :
	print("100보다 작군요.")

	
100보다 작군요.
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-01.py ===========
거짓이므로 이 문장은 안 보이겠죠?
프로그램 끝
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-02.py ===========
프로그램 끝
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-03.py ===========
100보다 크군요.
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-04.py ===========
100보다 크군요,
거짓이면 이 문장도 보이겠죠?
프로그램 끝
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-05.py ===========
정수를 입력하세요 : 125
홀수를 입력했군요.
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-06.py ===========
50보다 크고 100보다 작군요.
>>> 
======== RESTART: C:/Users/AISASE/Documents/JY_IDLE/turtle_leftright.py ========
Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/turtle_leftright.py", line 5, in <module>
    if l :
NameError: name 'l' is not defined
>>> 
======== RESTART: C:/Users/AISASE/Documents/JY_IDLE/turtle_leftright.py ========
명령을 입력하시오: l
>>> r
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    r
NameError: name 'r' is not defined
>>> 
========== RESTART: C:/Users/AISASE/Documents/JY_IDLE/luggage_Price.py =========
짐의 무게는 얼마입니까? 30
수수료 : 20000
감사합니다.
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-06.py ===========
50보다 크고 100보다 작군요.
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-07.py ===========
점수를 입력하세요 : 75
C
학점입니다. ^^
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code05-06.py ===========
와~ 100보다 크군요.
>>> 