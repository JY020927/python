Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=100
>>> a
100
>>> b=50
>>> b
50
>>> a="hello"
>>> a
'hello'
>>> type(a)
<class 'str'>
>>> a=100
>>> a
100
>>> type(a)
<class 'int'>
>>> a=3.14
>>> typ(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    typ(a)
NameError: name 'typ' is not defined
>>> type(a)
<class 'float'>
>>> a=100
>>> b=50
>>> result=a+b
>>> print(result)
150
>>> print(a, '+', b, '=', result)
100 + 50 = 150
>>> result=a-b
>>> print(a, '-', b, '=', result)
100 - 50 = 50
>>> result=a*b
>>> print(a, '*', b, '=', result)
100 * 50 = 5000
>>> result=a/b
>>> print(a, '/', b, '=', result)
100 / 50 = 2.0
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code02-01.py ===========
100 + 50 = 150
100 - 50 = 50
100 * 50 = 5000
100 / 50 = 2.0
>>> 
============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code02-02.py ===========

============ RESTART: C:/Users/AISASE/Documents/JY_IDLE/Code02-03.py ===========
첫 번째 숫자를 입력하세요 : 
Traceback (most recent call last):
  File "C:/Users/AISASE/Documents/JY_IDLE/Code02-03.py", line 1, in <module>
    a=int(input("첫 번째 숫자를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> data = '안녕' + \
             '     hello !!' + \
             'bye'
>>> data
'안녕     hello !!bye'
>>> print(data)
안녕     hello !!bye
>>> 
>>> 
>>> import turtle
>>> 
>>> turtle.shape('turtle')
>>> 
>>> 
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape('turtle')
>>> t.forward(50)
>>> t.fd(80)
>>> t.right(70)
>>> t.fd(100)
>>> t.baclward(200)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t.baclward(200)
AttributeError: 'Turtle' object has no attribute 'baclward'
>>> t.backward(200)
>>> t.left(120)
>>> t.left(90)
>>> t.left(30)
>>> t.fd(200)
>>> t.left(90)
>>> t.fd(200)
>>> t.left(90)
>>> t.fd(200)
>>> t.left(90)
>>> t.fd(200)
>>> 
>>> import turtle
>>> t.turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t.turtle.Turtle()
AttributeError: '_TurtleImage' object has no attribute 'Turtle'
>>> t.turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t.turtle.Turtle()
AttributeError: '_TurtleImage' object has no attribute 'Turtle'
>>> import turtle
>>> t.turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t.turtle.Turtle()
AttributeError: '_TurtleImage' object has no attribute 'Turtle'
>>> import turtle
>>> t=turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t=turtle.Turtle()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3815, in __init__
    RawTurtle.__init__(self, Turtle._screen,
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2558, in __init__
    self._update()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>>  import turtle
>>> t=turtle.Turtle()
>>> t.shape('turtle')
SyntaxError: unexpected indent
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape('turtle')
SyntaxError: multiple statements found while compiling a single statement
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape('turtle')
>>> t.fd(80)
>>> t.left(90)
>>> t.fd(80)
>>> t..left(90)
SyntaxError: invalid syntax
>>> t.left(90)
>>> t.fd(80)
>>> t.left(90)
>>> t.fd(80)
>>> t.up()
>>> t.clear()
>>> t.home()
>>> t.circle(100)
>>> t.home()\


	  
>>> t.home()
>>> t.circle(100)
>>> t.shape('arrow')
>>> t.shape('turtle')
>>> t.color('orange')
>>> t.fd(70)
>>> t.pencolor('purple')
>>> t.pensize(5)
>>> t.fd(60)
>>> 
>>> import turtle
>>> t=turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    t=turtle.Turtle()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3815, in __init__
    RawTurtle.__init__(self, Turtle._screen,
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2558, in __init__
    self._update()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> t.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    t.shape('turtle')
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2779, in shape
    self._update()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2662, in _update
    self._drawturtle()
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3012, in _drawturtle
    screen._drawpoly(titem, shape, fill=fc, outline=oc,
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 513, in _drawpoly
    self.cv.coords(polyitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\AISASE\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 