import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# incorrect
'''
def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(n + 1):
        total = total * i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')
'''        

# correct

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total = total * i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')



# Write log messages to a text file
'''
import logging
logging.basicConfig(filename = 'myProgramLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
'''

# To disable logging at once, add the below
'''
logging.disable(logging.CRITICAL)
'''
