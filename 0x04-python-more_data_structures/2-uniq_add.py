#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    summ = 0

    for i in my_list:
        if newlist.count(i) == 0:
            newlist.append(i)
            summ = summ + i
    return summ
