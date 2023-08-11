#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("Number of argument(s): 0.")
        print("No arguments.")
    elif num_args == 1:
        print("Number of argument(s): 1.")
        print("1 argument:")
    else:
        print("Number of argument(s): {}.".format(num_args))
        print("{} arguments:".format(num_args))

    for idx, arg in enumerate(argv, start=1):
        print("{}: {}".format(idx, arg))

