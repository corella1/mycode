#!/usr/bin/python3

calc1 = 0.0
calc2 = 0.0
operation = " "

while (calc1 != "q"):
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    calc1 = calc1.upper()
    if calc1 == "Q":
        break
    calc1 = float(calc1)
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input()
    calc2 = calc2.lower()
    if calc2 == "q":
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))

    elif operation == "-":
       print("\n" + str(calc1) + " - " + str(calc2) + " - " + str(calc1 - calc2))

    else:
       print("\n Not a valid entry. Restarting...")
