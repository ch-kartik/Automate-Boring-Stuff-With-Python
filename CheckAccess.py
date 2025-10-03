# checking Access


username = input('Enter username >')
password = 'swordfish'

if username == 'Mary':
  print('Hello, Mary')
  if password == 'swordfish':
    print('Access granted')
  else:
    print('Access denied')
else:
  user = input('Login as an admin >')
  if user.lower() == 'admin':
    print('Hello, Admin. Welcome')
  else:
    print('Please enter correct credentials')


# if, elif and else
'''
username = 'Mary'
password = 'swordfish'
if username == 'Mary':
  print('Hello, Mary')
  if password == 'swordfish':
    print('Access granted.')
  else:
    print('Access denied.')    


name = 'Alicea'
if name == 'Alice':
  print('Hi, Alice.')
else:
  print('Hello, stranger')



name = 'Alice'
age = 33
if name == 'Alice':
  print('Hello, Alice.')
elif age < 12:
  print('You are not Alice, kiddo.')


'''



