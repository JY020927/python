Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> slist = ["두부", "양배추", "딸기", "사과", "토마토"]
>>> slist
['두부', '양배추', '딸기', '사과', '토마토']
>>> type(slist)
<class 'list'>
>>> slist[0]
'두부'
>>> slist[3]
'사과'
>>> slist[2]
'딸기'
>>> slist[-1]
'토마토'
>>> slist[-3]
'딸기'
>>> slist[-2]
'사과'
>>> squares = [0,1,4,9,16,25,36,49]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49]
>>> type(squares)
<class 'list'>
>>> squares[3:6]
[9, 16, 25]
>>> squares[1:2]
[1]
>>> myList = [0,1,2,3,4,5,6,7]
>>> myList
[0, 1, 2, 3, 4, 5, 6, 7]
>>> type(myList)
<class 'list'>
>>> myList[3:6]
[3, 4, 5]
>>> alist = ["홍길동",3,5,[1,2],"이길동"]
>>> alist
['홍길동', 3, 5, [1, 2], '이길동']
>>> type(alist)
<class 'list'>
>>> alist[1:5]
[3, 5, [1, 2], '이길동']
>>> aa = [10,20,30,40]
>>> print("aa[-1]은 %d, aa[-2]는 %d" % (aa[-1], aa[-2]))
aa[-1]은 40, aa[-2]는 30
>>> aa = [10,20,30,40]
>>> aa[0:3]
[10, 20, 30]
>>> aa[2:4]
[30, 40]
>>> aa =[10,20,30,40]
>>> aa[2:]
[30, 40]
>>> aa[:2]
[10, 20]
>>> aa = [10,20,30]
>>> bb = [40,50,60]
>>> aa+bb
[10, 20, 30, 40, 50, 60]
>>> aa*3
[10, 20, 30, 10, 20, 30, 10, 20, 30]
>>> aa = [10,20,30,40,50,60,70]
>>> aa[::2]
[10, 30, 50, 70]
>>> aa[::-2]
[70, 50, 30, 10]
>>> aa[::-1]
[70, 60, 50, 40, 30, 20, 10]
>>> aa = [10,20,30]
>>> a[1] = 200
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a[1] = 200
NameError: name 'a' is not defined
>>> aa[1]=200
>>> aa
[10, 200, 30]
>>> aa=[10,20,30]
>>> aa[1:2] = [200, 201]
>>> aa
[10, 200, 201, 30]
>>> aa=[10,20,30]
>>> aa[1] = [200,201]
>>> aa
[10, [200, 201], 30]
>>> aa=[10,20,30]
>>> aa
[10, 20, 30]
>>> 
=========== RESTART: C:/Users/AISASE/Documents/JY_IDLE/기말_7장연습문제2번.py ==========
543
>>> import random
>>> random.randrange(2)
0
>>> random.randint(0,1)
0
>>> aa = [10,20,30]
>>> del(aa[1])
>>> aa
[10, 30]
>>> aa[1]
30
>>> aa = [10,20,30,40,50]
>>> aa
[10, 20, 30, 40, 50]
>>> aa[1:4]
[20, 30, 40]
>>> aa[1:4] = []
>>> aa
[10, 50]
>>> aa = [10,20,30]; aa = []; aa
[]
>>> aa = [10,20,30]; aa = None; aa
>>> 
>>> 
>>> 
>>> aa = [10,20,30]; del(aa); aa
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    aa = [10,20,30]; del(aa); aa
NameError: name 'aa' is not defined
>>> aa= None
>>> aa
>>> type(aa)
<class 'NoneType'>
>>> del(aa)
>>> aa
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    aa
NameError: name 'aa' is not defined
>>> type(aa)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    type(aa)
NameError: name 'aa' is not defined
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code07-05.py ===========
현재 리스트 : [30, 10, 20]
append(40) 후의 리스트 : [30, 10, 20, 40]
pop()으로 추출한 값 : 40
pop() 후의 리스트 : [30, 10, 20]
sort() 후의 리스트 : [10, 20, 30]
reverse() 후의 리스트 : [30, 20, 10]
20값의 위치 : 1
insert(2, 222) 후의 리스트 : [30, 20, 222, 10]
remove(222)후의 리스트 : [30, 20, 10]
extend([77, 88, 77]) 후의 리스트 : [30, 20, 10, 77, 88, 77]
77값의 개수 : 2
>>> myList = [30,10,20]
>>> myList
[30, 10, 20]
>>> newlist
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    newlist
NameError: name 'newlist' is not defined
>>> newlist = shorted(myList)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    newlist = shorted(myList)
NameError: name 'shorted' is not defined
>>> newlist = sorted(myList)
>>> newlist
[10, 20, 30]
>>> myList.sort()
>>> mylist
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    mylist
NameError: name 'mylist' is not defined
>>> myList
[10, 20, 30]
>>> aa = [10,20,30]
>>> aa = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9,10,11,12]]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> aa
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code07-06.py ===========
  1   2   3   4 Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/Code07-06.py", line 14, in <module>
    priint("")
NameError: name 'priint' is not defined
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code07-06.py ===========
  1   2   3   4 
  5   6   7   8 
  9  10  11  12 
>>> tt1 =(10,20,30)
>>> tt1
(10, 20, 30)
>>> type(tt1)
<class 'tuple'>
>>> tt2 = 10,20,30
>>> tt2
(10, 20, 30)
>>> type(tt2)
<class 'tuple'>
>>> tt3(10)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    tt3(10)
NameError: name 'tt3' is not defined
>>> tt3 = (10)
>>> tt3
10
>>> type(tt3)
<class 'int'>
>>> tt4=10
>>> tt4
10
>>> type(tt4)
<class 'int'>
>>> tt5(10,)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    tt5(10,)
NameError: name 'tt5' is not defined
>>> tt5= (10,)
>>> tt5
(10,)
>>> type(tt5)
<class 'tuple'>
>>> tt6 = 10,
>>> tt6
(10,)
>>> type(tt6)
<class 'tuple'>
>>> tt1
(10, 20, 30)
>>> tt1.append(40)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    tt1.append(40)
AttributeError: 'tuple' object has no attribute 'append'
>>> tt1[0]
10
>>> tt1[40]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    tt1[40]
IndexError: tuple index out of range
>>> del(tt1[0])
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    del(tt1[0])
TypeError: 'tuple' object doesn't support item deletion
>>> del(tt1)
>>> type(tt1)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    type(tt1)
NameError: name 'tt1' is not defined
>>> del(tt2)
>>> type(tt2)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    type(tt2)
NameError: name 'tt2' is not defined
>>> tt1 = (10,20,30,40)
>>> tt1[0]
10
>>> tt1[0] + tt1[1] + tt1[2]
60
>>> tt1[1:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> tt1[1:3]
(20, 30)
>>> tt1[1:]
(20, 30, 40)
>>> tt1[:3]
(10, 20, 30)
>>> tt2 = ('A', 'B')
>>> tt2
('A', 'B')
>>> tt1 = (10,20,30,40)
>>> tt1+tt2
(10, 20, 30, 40, 'A', 'B')
>>> tt2 * 3
('A', 'B', 'A', 'B', 'A', 'B')
>>> tt = ((1,2,3),
              (4,5,6),
              (7,8,9))
>>> 
>>> tt
((1, 2, 3), (4, 5, 6), (7, 8, 9))
>>> 