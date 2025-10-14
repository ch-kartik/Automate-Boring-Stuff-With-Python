
import random, sys

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'

while True:
    print('Ask yes or no question:')
    user_response = input('>')
    if user_response == 'no':
        print('Sure, try again later.')
        sys.exit()
    elif user_response == 'yes':
        r = random.randint(1, 9)
        fortune = get_answer(r)
        print(fortune)
    else:
        print('Enter either yes or no')
        continue

    

