#!/usr/bin/python3
""" The class Student module documentation """


class Student:
    """ Create student instances """

    def __init__(self, first_name, last_name, age):
        """ Initialise the function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            dict_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        dict_list[satr] = obj[satr]
            return dict_list

        return obj

    def reload_from_json(self, json):
        """ Replace all attributes of the Student """
        for atr in json:
            self.__dict__[atr] = json[atr]
