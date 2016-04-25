"""
Write a program to calculate expression:

1 + 2a    4(b + c)(5 - d - e)     7     2
------  + ------------------- - 6(- + h)
  3               f               g
"""

from __future__ import division

a = 32
b = 37.2
c = -102.345
d = 45
e = 11
f = 3
g = 0.002
h = 11

answer = ((1+2*a)/3)+((4*(b+c)*(5-d-e))/f)-(6*((7/g + h)**2))
print answer
