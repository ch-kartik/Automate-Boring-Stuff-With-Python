'''
import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

'''

# This is a random dice roll

import random, sys
try:
    for i in range(1, 6):
        random_number = random.randint(1, 6)

        def get_random_dice_roll():
                return random_number

        print(get_random_dice_roll())

except Keyboardnterrupt:
    sys.exit()
