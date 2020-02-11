Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['red', 'green', 'blue']
>>> L1 = ['black', 'grey', 'white']
>>> ####################################
>>> # Operators
>>> L + L1
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L
['red', 'green', 'blue']
>>> L1
['black', 'grey', 'white']
>>> L2 = L + L1
>>> L2
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L * 2
['red', 'green', 'blue', 'red', 'green', 'blue']
>>> 'red' in L
True
>>> len(L + L1)
6
>>> # del L[0]
>>> # del L
>>> ###################################
>>> # Accessability
>>> L[1]
'green'
>>> L[-1]
'blue'
>>> L[:3]
['red', 'green', 'blue']
>>> L[1:]
['green', 'blue']
>>> L[::-1]
['blue', 'green', 'red']
>>> # Replacements
>>> L[0] = 'orange'
>>> L
['orange', 'green', 'blue']
>>> L[-1][2] = 'x'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    L[-1][2] = 'x'
TypeError: 'str' object does not support item assignment
>>> ######################################
>>> L
['orange', 'green', 'blue']
>>> L.append('red')
>>> L
['orange', 'green', 'blue', 'red']
>>> L.append('yellow')
>>> L
['orange', 'green', 'blue', 'red', 'yellow']
>>> L.insert(1, 'maroon')
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow']
>>> L2
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L1
['black', 'grey', 'white']
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow']
>>> L1
['black', 'grey', 'white']
>>> L.append(L1)
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow', ['black', 'grey', 'white']]
>>> L.pop()
['black', 'grey', 'white']
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow']
>>> L.extend(L1)
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow', 'black', 'grey', 'white']
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow', 'black', 'grey', 'white']
>>> L.pop()
'white'
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow', 'black', 'grey']
>>> L.pop()
'grey'
>>> L
['orange', 'maroon', 'green', 'blue', 'red', 'yellow', 'black']
>>> L.pop(2)
'green'
>>> L.remove('red')
>>> L
['orange', 'maroon', 'blue', 'yellow', 'black']
>>> L.index('blue')
2
>>> L.index('white')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    L.index('white')
ValueError: 'white' is not in list
>>> L.find('white')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    L.find('white')
AttributeError: 'list' object has no attribute 'find'
>>> 'white' in L
False
>>> L.append('black')
>>> L.insert(3, 'black')
>>> L
['orange', 'maroon', 'blue', 'black', 'yellow', 'black', 'black']
>>> L.count('black')
3
>>> ############################
>>> L
['orange', 'maroon', 'blue', 'black', 'yellow', 'black', 'black']
>>> reversed(L)
<list_reverseiterator object at 0x0000020798B5F668>
>>> list(reversed(L))
['black', 'black', 'yellow', 'black', 'blue', 'maroon', 'orange']
>>> L
['orange', 'maroon', 'blue', 'black', 'yellow', 'black', 'black']
>>> L.reverse()
>>> L
['black', 'black', 'yellow', 'black', 'blue', 'maroon', 'orange']
>>> sorted(L)
['black', 'black', 'black', 'blue', 'maroon', 'orange', 'yellow']
>>> L
['black', 'black', 'yellow', 'black', 'blue', 'maroon', 'orange']
>>> L.sort()
>>> L
['black', 'black', 'black', 'blue', 'maroon', 'orange', 'yellow']
>>> L.sort(reverse=True)
>>> L
['yellow', 'orange', 'maroon', 'blue', 'black', 'black', 'black']
>>> 
