#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first = None

    if sentence:
        length = len(sentence)
        first = sentence[0]
    else:
        length = 0
        first = None
    print("Length: {:d} - First: {}".format(length, first))
    return (length, first)
