#!/usr/bin/python3

loginfail = 0
loginpass = 0


keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

keystone_file_lines = keystone_file.readlines()

for line in keystone_file_lines:
    if "- - - -] Authorization failed" in line:
        loginfail += 1
        words = line.split()

    if "- - - -] POST" in line:
        loginpass += 1

print("The number of failed log in attempts is " + str(loginfail))
print("The number of successful log in attempts is " + str(loginpass))
print("Failed IP address " + words[-1])

