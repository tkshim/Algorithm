#!/usr/bin/env python
#coding: utf-8

@profile

def multiplication(x):
    total = 1
    while x >=1:
        total *=  x
        x -= 1
    return total

if __name__ == '__main__':
    print multiplication(30)
