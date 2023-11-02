#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

argc = len(argv) - 1

if argc == 0:
    print("No arguments passed.")
elif argc == 1:
    print("1 argument passed:")
else:
    print("{} arguments passed:".format(argc))

for i, arg in enumerate(argv[1:], start=1):
    print("{}: {}".format(i, arg))
