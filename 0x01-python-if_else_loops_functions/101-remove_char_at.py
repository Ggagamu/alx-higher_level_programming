#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    ind = 0
    str_copy = ""
    for element in str:
        if ind == n:
            ind += 1
            continue
        str_copy += str[ind]
        ind += 1
    return str_copy
