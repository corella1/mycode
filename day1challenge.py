#!/usr/bin/python3

pets = [2, "cats", 3, "dogs"]

print("I have " + str(pets[2]) +" " + pets[1] + " and " + str(pets[0]) + " " + pets[3] + ".")

print("I have {2} {1} and {0} {3}.".format(*pets))


