#/usr/bin/env python
#coding: utf-8

def find_small_index(array_list):
    small_number = array_list[0]
    index = 0
    for i in range(1, len(array_list)):
        if array_list[i] < small_number:
            small_number = array_list[i]
            index = i
    return index

def sort_array(array_list):
    new_array = []
    while array_list:
        small_index = find_small_index(array_list)
        new_array.append(array_list.pop(small_index))
    return new_array

if __name__ == '__main__':
    temp_list001 = [6,3,0,11,3,1]
    print 'Index of Small Number is :', find_small_index(temp_list001)
    print 'New array is :', sort_array(temp_list001)
