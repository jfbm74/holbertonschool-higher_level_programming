#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx >= 0 and idx <= len(my_list):
            my_cpylst = my_list.copy()
            my_cpylst[idx] = element
            return (my_cpylst)
        else:
            return (my_list)
