#!/usr/bin/python3
import sys
suma = 0

for i in sys.argv[1:]:
    suma = suma + int(i)

print("{}".format(suma))
