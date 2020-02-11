Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> type(s)
<class 'str'>
>>> ###################################
>>> # Operators
>>> s + '123'
'python123'
>>> s * 3
'pythonpythonpython'
>>> "tho" in s
True
>>> "app" in s
False
>>> len(s)
6
>>> ########################################
>>> # Accessability
>>> s[0]
'p'
>>> s[-1]
'n'
>>> s[5]
'n'
>>> s[3]
'h'
>>> s[1:5]
'ytho'
>>> s[2:5]
'tho'
>>> s[-5:-2]
'yth'
>>> s[:3]
'pyt'
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> s[1:5:2]
'yh'
>>> s[::-1]
'nohtyp'
>>> s[2:5:-1]
''
>>> s1 = s[2:5]
>>> s1[::-1]
'oht'
>>> s[2:5][::-1]
'oht'
>>> ########################################################################
>>> s1 = "123"
>>> s2 = "sdfa"
>>> s3 = "34d"
>>> s4 = ' '
>>> s5 = "Q@#$"
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> ##
>>> s1.isupper()
False
>>> s1.isdigit()
True
>>> s1.isdigit()
True
>>> s3.isdigit()
False
>>> s3.isalnum()
True
>>> s4.isspace()
True
>>> s5.isalpha()
False
>>> site = "www.google.com"
>>> site.startswith('www')
True
>>> site.endswith('txt')
False
>>> ##
>>> s
'python'
>>> s.find('o')
4
>>> s.index('o')
4
>>> s.find('a')4
SyntaxError: invalid syntax
>>> s.find('a')
-1
>>> s.index('a')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.index('a')
ValueError: substring not found
>>> s6 = 'apples'
>>> s6.find('p')
1
>>> s7 = 'mississippi'
>>> s7.count('s')
4
>>> s7.count('ss')
2
>>> ip = '198-90-23-1'
>>> ip.replace('-', '.')
'198.90.23.1'
>>> amt = '12,34,456.00'
>>> amt = int(amt) + int(amt) * 0.1
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    amt = int(amt) + int(amt) * 0.1
ValueError: invalid literal for int() with base 10: '12,34,456.00'
>>> amt.replace(',', '')
'1234456.00'
>>> amt = int(amt) + int(amt) * 0.1
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    amt = int(amt) + int(amt) * 0.1
ValueError: invalid literal for int() with base 10: '12,34,456.00'
>>> amt = float(amt) + float(amt) * 0.1
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    amt = float(amt) + float(amt) * 0.1
ValueError: could not convert string to float: '12,34,456.00'
>>> amt.replace(',', '')
'1234456.00'
>>> amt
'12,34,456.00'
>>> amt2 = amt.replace(',', '')
>>> amt2
'1234456.00'
>>> amt = float(amt) + float(amt) * 0.1
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    amt = float(amt) + float(amt) * 0.1
ValueError: could not convert string to float: '12,34,456.00'
>>> amt = float(amt2) + float(amt2) * 0.1
>>> amt
1357901.6
>>> text = 'Tau is a circle constant equal to 2π'
>>> text.split()
['Tau', 'is', 'a', 'circle', 'constant', 'equal', 'to', '2π']
>>> text.count(' ')
7
>>> len(text.split())
8
>>> L = ['12', '04', '2020']
>>> '/'.join(L)
'12/04/2020'
>>> text
'Tau is a circle constant equal to 2π'
>>> text.split('a')
['T', 'u is ', ' circle const', 'nt equ', 'l to 2π']
>>> 
