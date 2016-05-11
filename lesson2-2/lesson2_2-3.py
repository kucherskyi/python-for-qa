"""
Write a function that takes a list and returns a new list that contains all the
elements of the first list minus all the duplicates
"""

def remove_duplicates(li):
    if not isinstance(li, list):
        return 'Not a list'
    else:
        return [elem for elem in li if li.count(elem) == 1]

print (remove_duplicates([1, 2, 3, 4, 4, 6, 2]))