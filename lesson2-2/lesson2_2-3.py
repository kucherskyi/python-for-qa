"""
Write a function that takes a list and returns a new list that contains all the
elements of the first list minus all the duplicates
"""

def remove_duplicates(li):
    if not isinstance(li, list):
        return 'Not a list'
    else:
        dic = {}
        for elem in li:
            if not elem in dic:
                dic[elem] = 1
            else:
                dic[elem] +=1
        return [key for key, val in dic.items() if val == 1]

print (remove_duplicates([1, 2, 3, 4, 4, 6, 2]))