"""
Write a script to automatically generate directories and files (empty 6 files
with names task*.py where * is task number between 1 and 6) structure for
python-for-qa course. Result should look the following way:

\python-for-qa
    \lesson1
        task1.py
        ...
        task6.py
    \lesson2
"""

import os

for i in range(1,7):
    os.makedirs('a\lesson{}'.format(i))
    path = os.path.join(os.getcwd(),'a\lesson{}'.format(i))
    for t in range(1,7):
        file = open(os.path.join(path,'\task.py'),'w')
        