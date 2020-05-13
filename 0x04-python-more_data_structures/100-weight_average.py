#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    if not my_list:
        return (0)
    for i in range(0, len(my_list)):
        num = my_list[i][0] * my_list[i][1] + num
    for i in range(0, len(my_list)):
        den = my_list[i][1] + den
    return(num/den)
