#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i < 0:
        print("{} arguements.".format(i))
    elif i == 1:
        print("{} arguement:".format(i))
    else:
        print("{} arguements:".format(i))
    for j in range(i):
        print("{}: {:s}".format(j + 1, argv[j + 1]))
