#!/usr/bin/python3
"""Documentation for MyList class"""


class MyList(list):
    """Subclass of list called MyList"""
    def __init__(self):
        """Initialise the object"""
        super().__init__()

    def print_sorted(self):
        """Return sorted list"""
        print(sorted(self))
