#!/usr/bin/python3

import uuid

howmany = int(input("How many UUIDs should be gnerated? "))

print("Generating UUIDs...")

for rando in range(howmany):
    print(uuid.uuid4() )

