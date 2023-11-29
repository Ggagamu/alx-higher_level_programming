#!/usr/bin/python3
"""This is the "5-test_indentation" module documentation"""


def text_indentation(text):
    """splits a text followed by 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    director = 0
    for a in text:
        if director == 0:
            if a == ' ':
                continue
            else:
                director = 1
        if director == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                director = 0
            else:
                print(a, end="")
