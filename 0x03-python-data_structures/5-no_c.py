#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    else:
        new_string = []
        for char in my_string:
            if char.lower() != 'c' and char.upper() != 'C':
                new_string.append(char)
        return ''.join(new_string)
