#!/usr/bin/python3
"""The class Student documentation """


class Student:
    """ Create student instances """

    def __init__(self, first_name, last_name, age):
        """ Initialise function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns directory representation """
        obj = self.__dict__.copy()
        if isinstance(attrs, list):

            for attribute in attrs:
                if not isinstance(attribute, str):
                    return obj

            dict_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        dict_list[satr] = obj[satr]
            return dict_list

        return obj
