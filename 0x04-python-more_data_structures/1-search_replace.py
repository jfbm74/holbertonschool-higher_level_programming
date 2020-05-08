#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list.copy()
    idx = 0
    if search < len(my_list):
        for i in nlist:
            if i == search:
                nlist[idx] = replace
            idx = idx + 1
    return nlist
