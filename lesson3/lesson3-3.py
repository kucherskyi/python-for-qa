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


def dircreator():

    for i in range(1, 7):
        if not os.path.exists('homework\lesson{}'.format(i)):
            os.makedirs('homework\lesson{}'.format(i))
            path = os.path.join(os.getcwd(), 'homework\lesson{}'.format(i))
            for fold in range(1, 7):
                name_of_file = 'atask{}.py'.format(fold)
                path_to_file = os.path.join(path, name_of_file)
                file = open(path_to_file, 'w')
                if os.path.isfile(os.path.join(path, '__init__.py')):
                    pass
                else:
                    file = open(os.path.join(path, '__init__.py'), 'w')
        else:
            print 'Directories already exists!'
            break

dircreator()
