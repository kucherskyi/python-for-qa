"""
Write program to evaluate (a or not b) and (c or not a) expression for boolean
varibles a, b, c showing result for all possible variables combinations.
"""

for a in (True, False):
    for b in (True, False):
        for c in (True, False):
            print ((a or not b) and (c or not a))
