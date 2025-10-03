Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello, world!")
Hello, world!
print('Hello, world!')
Hello, world!
'42' + 3
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#2>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
2 + 2
4
2 + 3 * 6
20
(2 + 3) * 6
30
48565878 * 578453
28093077826734
2 ** 8
256
23 / 7
3.2857142857142856
23 // 7
3
23 % 7
2
2    +                2
4
(5 - 1) * ((7 + 1) / (3 - 1))
16.0
5 +
SyntaxError: invalid syntax
42 + 5 + * 2
SyntaxError: invalid syntax
'Hello, world!
SyntaxError: unterminated string literal (detected at line 1)
'Alice' + 'Bob'
'AliceBob'
'Alice' + 42
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#17>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
'Alice' + str(42)
'Alice42'
'Alice' * 5
'AliceAliceAliceAliceAlice'
'Alice' * 'Bob'
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#20>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
'Alice' * 5.0
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#21>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
spam = 40
spam
40
eggs = 2
spam + eggs
42
spam + eggs + spam
82
spam = spam + 2
spam
42
spam = 'Hello'
spam
'Hello'
spam = 'Goodbye'
spam
'Goodbye'

=========== RESTART: /home/kartik-ch/Data Engineering/Python/hello.py ==========
Hello, world!
What is your name?
>Kartik
It is good to meet you, Kartik
The length of your name is:
6
What is your age?
>4
You will be5in a year.

=========== RESTART: /home/kartik-ch/Data Engineering/Python/hello.py ==========
Hello, world!
What is your name?
>K
It is good to meet you, K
The length of your name is:
1
What is your age?
>4
You will be 5 in a year.
len('Hello')
5
len('My very energetic monster just scarfed nachos.')
46
len('')
0
print('I am ' + 29 + ' years old.')
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#36>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
'I am ' + 29 + ' years old.'
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#37>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
print('I am ' + str(29) + ' years old.')

I am 29 years old.
str(0)
'0'
str(-3.14)
'-3.14'
int('42')
42
int('-99')
-99
int(1.25)
1
int(1.99)
1
float('3.14')
3.14
float(10)
10.0
spam = input()
101
spam
'101'
spam = int(spam)
spam
101
spam * 10 / 5
202.0
spam * 10 // 5
202
int('99.99')
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#53>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '99.99'
int('twelve')
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#54>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'twelve'
int(7.7)
7
int(7.7) + 1
8
42 == '42'
False
42 == 42.0
True
42.0 == 0042.000
True
type(42)
<class 'int'>
type(42.0)
<class 'float'>
type('forty two')
<class 'str'>
name = 'Zophie'
type(name)
<class 'str'>
type(len(name))
<class 'int'>
len(name)
6
round(3.14)
3
round(3.15)
3
round(3.18)
3
>>> round(3.99)
4
>>> round(3.95)
4
>>> round(3.49)
3
>>> round(3.50)
4
>>> round(3.69)
4
>>> round(7.7)
8
>>> round(7.4)
7
>>> round(-2.2)
-2
>>> round(-2.5)
-2
>>> round(-2.8)
-3
>>> round(-2.6)
-3
>>> round(3.14, 1)
3.1
>>> round(3.14, 2)
3.14
>>> round(3.14, 3)
3.14
>>> round(7.7777, 3)
7.778
>>> abs(25)
25
>>> abs(-25)
25
>>> abs(-3.14)
3.14
>>> abs(0)
0
