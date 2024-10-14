#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv[1:]

    if not args:
        print("{}".format("0 arguments."))
    elif len(args) == 1:
        print("{}".format("1 argument:"))
        print("{}: {}".format(len(args), args[0]))
    else:
        print("{} {}".format(len(args), "arguments:"))
        for i in range(len(args)):
            print("{}: {}".format(i + 1, args[i]))
