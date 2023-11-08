def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    sum_weight = total_score = average = 0
    for tuple in my_list:
        sum_weight += tuple[1]
        total_score += tuple[0] * tuple[1]
        average = total_score / sum_weight
    return average
