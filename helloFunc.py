
# Function without arguments and parameters

'''
def hello():
    print('Good morning!')
    print('Good afternoon!')
    print('Good evening!')

hello()
hello()
print('ONE MORE TIME!')
hello()

'''



# Function with arguments and parameters

def say_hello_to(name):
    # Prints three greetings to the name provided
    print('Good morning, ' + name)
    print('Good afternoon, ' + name)
    print('Good evening, ' + name)


say_hello_to('Alice')
say_hello_to('Bob')
#print(name)    # This gives NameError 
