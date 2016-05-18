"""
Print a number of sentences in a file alice_in_wonderland.txt (a sentence
shall end in either a dot . or a tripple-dot ...)
"""

import re

with open('alice_in_wonderland.txt', 'r') as alice:
    list_of_sentences = re.split(r'\b\.?\.\.?(?=\s)', alice.read())


print ('Number of sentences is: {}' .format( len(list_of_sentences)))
