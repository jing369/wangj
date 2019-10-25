#!usr/bin/python
# -*- coding: utf-8 -*

# Python内建了reduce()函数。
def add(x,y):
    return x*10+y
a = reduce(add,[1,3,5])
print a



