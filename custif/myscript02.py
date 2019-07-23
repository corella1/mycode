#!/usr/bin/python3

rec = 'Your internet speed is as follows'

print('Which of the following speeds would you like? Please select an option below.')
print('Option 1: 10Mbps')
print('Option 2: 50Mbps')
print('Option 3: 75Mbps')
print('Option 4: 1Gb')

choice = input("Please provide your Option: ")

if choice == 'Option 1':
    rec = rec + ' Your speed has been set to 10Mbps'

elif choice == 'Option 2':
    rec = rec + ' Your speed has been set to 50Mbps'

elif choice == 'Option 3':
    rec = rec + ' Your speed has been set to 75Mbps'

elif choice == 'Option 4':
    rec = rec + ' Your speed has been set yo 1Gb'

else:
    rec = 'Please provide input again'

print(rec)    

