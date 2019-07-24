#!/usr/bin/python3

round = 0 

while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The life of _____"')

    answer = input()
    answer = answer.lower()

    if answer == 'brian':
        print('Correct')
        break

    elif answer == 'shrubbery':
        print('You gave the super secert answer!')
        break

    elif round == 3:
        print('Sorry, the answer was Brian.')
        break

    else:
        print('Sorry! Try again!')
