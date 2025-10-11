
#if-else and flow control
spam = True
spam
True
true
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#3>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
False = 2 + 2
SyntaxError: cannot assign to False
42 == 42
True
42 == 99
False
2 != 3
True
2 != 2
False
'hello' == 'hello'
True
'hello' == 'Hello'
False
'dog' != 'cat'
True
True == True
True
True != False
True
42 == 42.0
True
42 == '42'
False
42 < 100
True
>>> 42 > 100
False
>>> 42 < 42
False
>>> eggs = 42
>>> eggs <= 42
True
>>> my_age = 29
>>> my_age >= 10
True
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> not True
False
>>> not False
True
>>> not not not not True
True
>>> (4 < 5) and (5 < 6)
True
>>> (4 < 5) and (9 < 6)
False
>>> (1 == 2) or (2 == 2)
True

username = 'Mary'
password = 'swordfish'
if username == 'Mary':
  print('Hello, Mary')
  if password == 'swordfish':
    print('Access granted')
  else:
    print('Access denied')
    
