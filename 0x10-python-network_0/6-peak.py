#!/usr/bin/python3
""" Documentation for a module for a function that finds 
a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ Finds the peak integer of an un sorted list """
    sample_space = list_of_integers
    sample_space.sort()
    if sample_space:
        return sample_space[-1]
    else:
        return None
