import random
number_of_streaks = 0
result = 0
for experiment_number in range(10000):
    # Code that creates a list of 100 'heads' or 'tails'
    coin_toss_result = []
    for i in range(100): # 100 tosses
        result = random.randint(0, 1)
        if result == 0:
            coin_toss_result.append('T')
        elif result == 1:
            coin_toss_result.append('H')
    #print(coin_toss_result)

    # Code that checks if there is a streak of 6 heads or tails in a row
    for j in range(0,95):   # Stop at 94 to avoid out-of-bounds error
        if coin_toss_result[j:j+6] == ['H', 'H', 'H', 'H', 'H', 'H']:
            #print('Its a streak of heads')
            number_of_streaks += 1
        elif coin_toss_result[j:j+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            #print('Its a streak of tails')
            number_of_streaks += 1


print('Chance of streak: %s%%' % (number_of_streaks / 10000 * 100))

