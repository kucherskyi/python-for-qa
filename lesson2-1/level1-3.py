"""
Print unique elements from any given list or tuple.
"""

def unique(given):
    
    return "List of unique elements :{}".format(list(set(given)))

"""
Example
"""
a = [1,'aaa', 2, 3, 4, 5,'aaa', 6,5,6,3,4,2]
b = (1,'aaa', 2, 3, 4, 5,'aaa', 6,5,6,3,4,2)

print unique(a)
print unique(b)