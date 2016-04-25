"""
Print unique elements from any given list or tuple.
"""

import random


def unique(given):

    return "List of unique elements :{}".format(list(set(given)))

"""
Examples
"""

l = [random.randint(0, 100) for i in range(50)]
t = tuple(random.randint(0, 100) for i in range(50))

print "List " + str(l)
print unique(l)
print "Tuple " + str(t)
print unique(t)
