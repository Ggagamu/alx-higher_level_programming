#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, valu in sorted(a_dictionary.items()):
        if valu == value:
            del a_dictionary[key]
    return a_dictionary
