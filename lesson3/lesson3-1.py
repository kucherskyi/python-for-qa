"""
Write a program to generate list with all numbers divisible by 2 and 3 between
1 and 10000 using two approaches:
- list comprehension
- filter function
"""

print [x for x in xrange(1, 10000) if x % 2 == 0 and x % 3 == 0]
print filter(lambda x: x % 2 == 0 and x % 3 == 0, xrange(1, 10000))
