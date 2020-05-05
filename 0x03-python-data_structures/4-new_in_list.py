#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        my_cpylist = my_list.copy()
        if len(my_list) < idx or idx < 0:
            return my_cpylist
        else:
            my_cpylist[idx] =  element
            return my_cpylist
