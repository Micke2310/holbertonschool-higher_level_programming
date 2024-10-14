#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv[1:]

    if not args:
        print("0 arguments.")
    elif len(args) == 1: 
        print("1 argument:")
        print(f"{len(args)}: {args[0]}")
    else:
        print(f"{len(args)} arguments:")
        for i in range(len(args)):
            print(f"{i}: {args[i]}")
