#!/usr/bin/env python
#coding: utf-8

@profile
def fact2(x):
    #print x
    if x == 1:return 1
    return x * fact2(x-1)

if __name__ == '__main__':
    fact2(30)
