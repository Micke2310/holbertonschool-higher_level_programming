#!/usr/bin/python3
num = 0
for num in range(97, 123):
    if num == 101 or num == 113:
        continue
    alphabet = chr(num)
    print("{}".format(alphabet), end="")
