#!/usr/bin/python3

thisround = 0

while(True):
    print('What is the IPv4 address used to broadcast on a local network? ')
    answer = input()
    if answer == '255.255.255.255':
        print('correct')
        break
    elif thisround == 3:
        print('Sorry, the answer was 255.255.255.255')
        break
    else:
        print('Sorry. Try again!')
