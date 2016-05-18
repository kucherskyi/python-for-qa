"""
We need to decrease issues count and priority in Python for QA -
bugs list - Sheet1.csv. Write a program to decrease each issue priority to one
level (critical -> high, high -> medium, medium -> low), issues that have
low level now should be removed. Save result into new CSV file.
"""

import csv


def csv_parcer(file):

    with open(file, 'r') as logfile:
        reader = csv.DictReader(logfile)
        with open('new_{}'.format(file), 'wb') as csv_towrite:
            writer = csv.DictWriter(csv_towrite, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row['Priority'] == 'critical':
                    row['Priority'] = 'high'
                    writer.writerow(row)
                elif row['Priority'] == 'high':
                    row['Priority'] = 'medium'
                    writer.writerow(row)
                else:
                    pass
    print ('Done!')

csv_parcer('bugs_list.csv')
