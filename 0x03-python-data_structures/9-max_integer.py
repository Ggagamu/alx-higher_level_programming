#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_dig = my_lisy[0]
    for dig in my_list:
        if dig > max_dig:
            max_dig = dig
    return max_dig
