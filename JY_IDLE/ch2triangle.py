Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape('turtle')
>>> t.fd(30)
>>> t.fd(30)
>>> t.left(60)
>>> t.left(60)
>>> t.fd(60)
>>> t.left(120)
>>> t.fd(60)
>>> t.circle(50)
>>> t.right(90)
>>> t.right(90)
>>> t.circle(50)
>>> 
>>> print('100')
100
>>> print('%d' %100)
100
>>> print('100+100')
100+100
>>> print('%d' % (100+100))
200
>>> print('%d' % (100, 200))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('%d' % (100, 200))
TypeError: not all arguments converted during string formatting
>>> print('%d %d' % (100))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print('%d %d' % (100))
TypeError: not enough arguments for format string
>>> print('%d %d' % (100, 200))
100 200
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code03-01.py ===========
123
  123
00123
123.450000
  123.5
123.450
Python
    Python
>>> print('%d %5d %05d' % (123, 123, 123))
123   123 00123
>>> print('{0:d} {1:5d} {2:05d}'.format(123,123,123))
123   123 00123
>>> print('{2:d} {1:d} {0:d}'.format(100,200,300))
300 200 100
>>> 