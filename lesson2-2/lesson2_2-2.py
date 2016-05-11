"""
Write a function that takes a comma-separated string and returns the last
element (separated by the last comma) or the entire string, if there is no
comma in it.
"""

def coma(cs):
    if ',' in cs:
        return cs.split(',')[-1:]
    else:
        return cs
    
s = """Write a function that takes a comma-separated string and returns
the last element (separated by the last comma) or the entire string, if there
is no comma in it."""
print (coma(s))