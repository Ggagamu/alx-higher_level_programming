#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    weight_sum = 0
    total_score = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        weight_sum += weight
        total_score += score * weight
    return total_score / weight_sum
