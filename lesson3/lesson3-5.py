"""
Write a script to convert strings to date objects. Input list:
-11 Jan 2016
-4 April 2011
-11.03.2014
-03/24/91
Script should have defined supported dates formats. Conversion should be
in the loop.
"""

from datetime import datetime

dates = ['11 Jan 2016', '4 April 2011', '11.03.2014', '03/24/91']


def validator(dateitem):
    formats = ['%d %b %Y', '%d %B %Y', '%d.%m.%Y', '%m/%d/%y']
    for elem in dateitem:
        for i in formats:
            try:
                print 'Formatted data is {}'.format(datetime.strptime(elem, i))
            except ValueError:
                pass

validator(dates)
