import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('The value of guess is ' + guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('The integer value of toss returned is ' + str(toss))
if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'


if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('The value of guess is ' + guess + ' while value of toss is ' + str(toss))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
