Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello HPE')
Hello HPE
>>> # Numbers
>>> a = 10
>>> b = 5
>>> a
10
>>> b
5
>>> print(a)
10
>>> print(b)
5
>>> print(a , b)
10 5
>>> print('a = ', a)
a =  10
>>> print('b = ', b)
b =  5
>>> a
10
>>> a =12
>>> a
12
>>> a =10
>>> a
10
>>> ###########################################################
>>> # Operators
>>> a
10
>>> b
5
>>> a + b
15
>>> a - b
5
>>> a * b
50
>>> a / b
2.0
>>> a ** 2
100
>>> 5 % 3
2
>>> 5 / 3
1.6666666666666667
>>> 5 // 3
1
>>> a > b
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a == b * 2
True
>>> a != b
True
>>> a <= 10 and b == 5
True
>>> b == 5
True
>>> not b == 5
False
>>> a == 10 or b == 6
True
>>> a == 10 and b == 6
False
>>> ###################################################
>>> s = '234'
>>> type(s)
<class 'str'>
>>> type(a)
<class 'int'>
>>> s
'234'
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 10
244
>>> x = input('Enter a number: ')
Enter a number: 67
>>> x ** 2
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> type(x)
<class 'str'>
>>> int(x) ** 2
4489
>>> b = '1111'
>>> int(b)
1111
>>> int(b) + 13
1124
>>> int(b, 2)
15
>>> y = '123.23"
SyntaxError: EOL while scanning string literal
>>> y = '123.45'
>>> type(y)
<class 'str'>
>>> int(y)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(y)
ValueError: invalid literal for int() with base 10: '123.45'
>>> float(y)
123.45
>>> #######################################################3
>>> gcd(60, 30)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    gcd(60, 30)
NameError: name 'gcd' is not defined
>>> import math
>>> math.gcd(60, 30)
30
>>> math.sqrt(144)
12.0
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * (3.1416/180))
0.9999999999932537
>>> math.sin( 90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> #############################################
>>> a = 10
>>> b = math.sqrt(a)
>>> a == b * b
False
>>> a
10
>>> b
3.1622776601683795
>>> b ** 2
10.000000000000002
>>> 
