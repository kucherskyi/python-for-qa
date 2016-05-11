"""
Write a function to return the sum of the numbers in the array, returning 0
for an empty array. Since the number 13 is very unlucky, it does not count,
and numbers that come immediately after a 13 also do not count. Array could
contain strings and boolean values (do not count them too)
"""


def sum_list(arr):
    array_sum = 0
    array_edited = [elem for elem in arr if isinstance(elem, int) 
                    and not isinstance(elem, bool)]
    if len(array_edited) == 0:
        return 0

    if 13 in array_edited:
        for i in array_edited[:array_edited.index(13)]:
            array_sum += i
        return array_sum
    else:
        return sum(array_edited)

a = [1, 2, 2, 1, 5, 4, 2, 13, 'aaa',True, 'asd',False]
b = []
c = [1, 2, 2, 1]

print (sum_list(a))
print (sum_list(b))
print (sum_list(c))