"""
Write a function to return the sum of the numbers in the array, returning 0
for an empty array. Since the number 13 is very unlucky, it does not count,
and numbers that come immediately after a 13 also do not count. Array could
contain strings and boolean values (do not count them too)
"""


def sum_list(arr):
    
    array_sum = []
    for elem in arr:
        if elem == 13:
            break
        else:
            if isinstance(elem, int) and not isinstance(elem, bool):
                array_sum.append(elem)
    
    return sum(array_sum)

a = [1, 2, 2, 1, 5, 4, 2, 'aaa',True, 'asd',False]
b = []
c = [1, 2, 2,13, 1]

print (sum_list(a))
print (sum_list(b))
print (sum_list(c))