
# The Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result, sep = ' ', end = ' ')
        return result
        
    elif number % 2 != 0:
        result = 3 * number + 1
        print(result, sep = ' ', end = ' ')
        return result
        

print('Enter number: ')
try:
    num = int(input())
    print( num, sep = ' ', end = ' ')
    while num != 1:
        num = collatz(num)
except ValueError:
    print('Enter an integer')
    

    
    
