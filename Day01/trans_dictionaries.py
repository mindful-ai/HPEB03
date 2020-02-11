Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = {'name':'anil', 'age':35, 'country':'India' }
>>> D
{'name': 'anil', 'age': 35, 'country': 'India'}
>>> type(D)
<class 'dict'>
>>> D['name']
'anil'
>>> D['age']
35
>>> D['country']
'India'
>>> D['company']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    D['company']
KeyError: 'company'
>>> D['company
  
SyntaxError: EOL while scanning string literal
>>> D['company'] = 'Infosys'
>>> D
{'name': 'anil', 'age': 35, 'country': 'India', 'company': 'Infosys'}
>>> D.setdefault('gender', 'M')
'M'
>>> D
{'name': 'anil', 'age': 35, 'country': 'India', 'company': 'Infosys', 'gender': 'M'}
>>> D.remove('gender')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    D.remove('gender')
AttributeError: 'dict' object has no attribute 'remove'
>>> D.pop('gender')
'M'
>>> D
{'name': 'anil', 'age': 35, 'country': 'India', 'company': 'Infosys'}
>>> 'age' in D
True
>>> D.keys()
dict_keys(['name', 'age', 'country', 'company'])
>>> D.values()
dict_values(['anil', 35, 'India', 'Infosys'])
>>> D.items()
dict_items([('name', 'anil'), ('age', 35), ('country', 'India'), ('company', 'Infosys')])
>>> 
