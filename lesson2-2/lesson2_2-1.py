"""
Write a function which takes a string and returns its first 10 characters
concatenated with the last 10 characters.
"""

def concatenate(strings):
    if not isinstance(strings, str):
        return "Input is not string"
    else:
        return strings[:10] + strings[-10:]
    
print (concatenate('12345678912345678a'))