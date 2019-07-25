#!/usr/bin/env python3

user = input("would you like to quit: ")
while user.lower() != 'q':
    try:
        a = int(input("Please put an integer here\n"))
    except ValueError:
        print("That is not an integer")
        continue

    
    print( a + 20 )
    user = input("would you like to quit: ")
    if user.lower() == 'q':
        break


