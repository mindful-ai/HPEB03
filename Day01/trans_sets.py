Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'s', 'i', 'm', 'p'}
>>> s[0]
'm'
>>> S = set(s)
>>> S[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    S[0]
TypeError: 'set' object is not subscriptable
>>> type(S)
<class 'set'>
>>> ###################################################
>>> s1 = set('abcdef')
>>> s2 = set('defghi')
>>> s1
{'e', 'b', 'f', 'a', 'c', 'd'}
>>> s2
{'i', 'g', 'h', 'f', 'e', 'd'}
>>> s1.add('y')
>>> S1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    S1
NameError: name 'S1' is not defined
>>> s1
{'y', 'e', 'b', 'f', 'a', 'c', 'd'}
>>> s3 = {'y', 'z'}
>>> s2.update(s3)
>>> s2
{'y', 'i', 'g', 'h', 'z', 'f', 'e', 'd'}
>>> s2.remove('d')
>>> s2
{'y', 'i', 'g', 'h', 'z', 'f', 'e'}
>>> names = {'anil' ,'sunil'}
>>> names
{'anil', 'sunil'}
>>> names[0]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    names[0]
TypeError: 'set' object is not subscriptable
>>> s1
{'y', 'e', 'b', 'f', 'a', 'c', 'd'}
>>> s2
{'y', 'i', 'g', 'h', 'z', 'f', 'e'}
>>> s1 & s1
{'f', 'y', 'b', 'a', 'e', 'd', 'c'}
>>> s1 & s2
{'f', 'y', 'e'}
>>> s1 | s2
{'y', 'i', 'c', 'g', 'h', 'z', 'f', 'b', 'a', 'e', 'd'}
>>> s1 ^ s2
{'i', 'd', 'g', 'h', 'z', 'b', 'a', 'c'}
>>> s1.intersection(s2)
{'f', 'y', 'e'}
>>> s1.union(s2)
{'y', 'i', 'c', 'g', 'h', 'z', 'f', 'b', 'a', 'e', 'd'}
>>> s1
{'y', 'e', 'b', 'f', 'a', 'c', 'd'}
>>> s2
{'y', 'i', 'g', 'h', 'z', 'f', 'e'}
>>> 
