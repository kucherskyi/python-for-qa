"""
Write a program to calculate the number of times that the string 'hi' appears 
anywhere in the given string and change 'hi' to 'bye'. Case should be ignored.
"""

def count(string):
    print 'String "hi" appears for {} times'.format(string.count("hi"))
    print 'Replaced "hi" to "bye": \n{}'.format(string.replace('hi',"bye"))

"""
Example
"""
exampl = """Whirite a program hi hi  to hi calculate the number of times that 
the string 'hi' appears anywhere in the given string and change 'hi' to 'bye'. 
Case should be ignored."""

count (exampl)
