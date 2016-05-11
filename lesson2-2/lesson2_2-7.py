"""
Write a function to find out if the word is a palindrome.
"""

import string


def palindrome1(wrd):

    if wrd == ''.join(reversed(wrd)):
        return True
    else:
        return False


def palindrome2(wrd):
    """
    I've used string module to add possibility to check, whether a sentence
    is a palindrome, not only single word.
    """

    def striper(wr):
        wr = "".join(c for c in wr if c not in string.punctuation)
        wr = wr.lower().strip().replace(' ', '')
        return wr

    def checker(wrd):
        if len(wrd) < 2:
            return True
        if wrd[0] == wrd[-1]:
            return checker(wrd[1:-1])
        else:
            return False

    if isinstance(wrd, str):
        wrd = striper(wrd)
        return checker(wrd)
    else:
        return "not a string"


palindrom = 'A man, a plan, a canal, Panama!'

print (palindrome1(palindrom))
print (palindrome2(palindrom))
