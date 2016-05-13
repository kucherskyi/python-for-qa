"""
Write a function that takes a list and returns a new list that contains all the
elements of the first list minus all the duplicates
"""

import timeit
import random


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def remove_duplicates2(li):
    if not isinstance(li, list):
        return 'Not a list'
    else:
        return [elem for elem in li if li.count(elem) == 1]


def remove_duplicates(li):
    if not isinstance(li, list):
        return 'Not a list'
    else:
        dic = {}
        for elem in li:
            if elem not in dic:
                dic[elem] = 1
            else:
                dic[elem] += 1
        return [key for key, val in dic.items() if val == 1]

fu2 = [random.uniform(0, 100) for x in xrange(100)]
print fu2

wrapped = wrapper(remove_duplicates, fu2)
seco = timeit.timeit(wrapped, number=100000)
wrapped = wrapper(remove_duplicates2, fu2)
first = timeit.timeit(wrapped, number=100000)
print """
         First = {0};
         Second = {1};
         Second is faster in {2} times""".format(first, seco, first/seco)
# print (remove_duplicates([1, 2, 3,5 , 12,4, 4, 6, 31,31, 2, 3, 4, 4, 6, 21]))
