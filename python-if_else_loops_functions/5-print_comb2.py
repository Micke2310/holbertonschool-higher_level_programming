#!/usr/bin/python3
num = 0
for num in range(0, 100):
    if num == 99:
        print("{:02d}".format(num))
    else:
        print("{:02d}, ".format(num), end="")
