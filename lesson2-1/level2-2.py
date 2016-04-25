"""
Unite three lists to one and print it in reverse order:
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

united_list = list1 + list2 + list3

print united_list[::-1]
#or
united_list.reverse()
print united_list