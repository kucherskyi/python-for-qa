"""
Write a function that returns dictionary where keys are even numbers
between 1 and n and values are keys in square, by default n = 100
"""

return_dict = lambda x: {key:key ** 2 for key in xrange(1, x+1)}

print return_dict(100)
