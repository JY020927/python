Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(0,3,1):
	print("hello")

	
hello
hello
hello
>>> 
>>> for i in [0,1,2]:
	print("hello")

	
hello
hello
hello
>>> for i in range(0,3,1):
	print("%d: Hello " % i)

	
0: Hello 
1: Hello 
2: Hello 
>>> for i in range(1,4,1)
SyntaxError: invalid syntax
>>>  for i in range(1,4,1):
	 
SyntaxError: unexpected indent
>>> for i in range(1,4,1):
	print("%d: Hello " % i)

	
1: Hello 
2: Hello 
3: Hello 
>>> for i in range(0,3,1):
	print('%d : Hello'%(i+1))

	
1 : Hello
2 : Hello
3 : Hello
>>> for i in range(0,3,1):
	print("%d: hello" % (i+1))

	
1: hello
2: hello
3: hello
>>> for _ in range(0,3,1):
	print("Hello")

	
Hello
Hello
Hello
>>> for i in range(2, -1, -1):
	print("%d: hello" % i)

	
2: hello
1: hello
0: hello
>>> for i in range(1, 6,1) :
	print("%d " % i, end = " ")

	
1  2  3  4  5  
>>> for i in range(1, 6,1) :
	print("%d " % i)

	
1 
2 
3 
4 
5 
>>> 
========== RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-02(1).py ==========
Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/Code06-02(1).py", line 4, in <module>
    hap = hap+i
NameError: name 'hap' is not defined
>>> 
========== RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-02(2).py ==========
1에서 10까지의 합계 : 55
>>> for c in "abcdef":
	print(c, end=" ")

	
a b c d e f 
>>> a = "hello"
>>> 
>>> 
>>> 
>>> a[0]
'h'
>>> a[3]
'l'
>>> a[4]
'o'
>>> for c in "hello":
	print(c, end="  ")

	
h  e  l  l  o  
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-03.py ===========
500과 1000사이에 있는 홀수의 합계 : 187500
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-03.py ===========
500과 1000사이에 있는 홀수의 합계 : 187500
0과 100사이에 있는 7의 배수 합계 : 0
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-03.py ===========
500과 1000사이에 있는 홀수의 합계 : 187500
0과 100사이에 있는 7의 배수 합계 : 735
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-05.py ===========
Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/Code06-05.py", line 2, in <module>
    num1, num2, num3 = 0, 0,
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code06-05.py ===========
시작값을 입력하세요 : 2
끝값을 입력하세요 : 300
증가값을 입력하세요 : 3
2에서 300까지 3씩 증가시킨 값의 합계 : 15050
>>> 