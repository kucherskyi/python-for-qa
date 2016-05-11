"""
Write a function that takes a comma-separated string and returns the last
element (separated by the last comma) or the entire string, if there is no
comma in it.
"""

coma = lambda cs:cs.split(',')[-1:]
    
s = """Write a function that takes a comma-separated string and returns
the last element (separated by the last comma) or the entire string if there
is no comma in, it."""

print (coma(s))