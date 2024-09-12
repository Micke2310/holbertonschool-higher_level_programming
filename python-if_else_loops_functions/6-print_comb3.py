#!/usr/bin/python3

A = range(0, 10)
B = range(0, 10)

for a in A:
    for b in B:
        if a < b:
            if a == 8 and b == 9:
                print("{}{}".format(a, b))
            else:
                print("{}{}, ".format(a, b), end="")
