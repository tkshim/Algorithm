#!/usr/bin/env python
#coding: utf-8
sample_data = ['0AFHD', '1SAFS', 'constitute', 'Sedge', 'Eflux', 'Whim']
key = 'Eflux'

def sort_data(raw_data_list):
    values = sorted(raw_data_list, key=str.lower)
    keys = [ i for i in range(len(raw_data_list))]
    sorted_dict = dict(zip(keys, values))
    return sorted_dict

def search_index(sorted_dict, key, start_n):
    index_n = -1
    for i in range(start_n, len(sorted_dict)):
        if sorted_dict[i] == key:
            index_n = i
            break
    return index_n

if __name__ == '__main__':
    sorted_dict = sort_data(sample_data)
    print search_index(sorted_dict, key)
