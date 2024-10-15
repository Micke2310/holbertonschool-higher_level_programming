#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0

    for i in sys.argv[1:]:
        suma = suma + int(i)

    print("{}".format(suma))
