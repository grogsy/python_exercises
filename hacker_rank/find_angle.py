# Problem desc: https://www.hackerrank.com/challenges/find-angle/problem
from math import acos, degrees, hypot

AB = int(input())
BC = int(input())
M = hypot(AB, BC) / 2
# Law of Cosines: https://en.wikipedia.org/wiki/Law_of_cosines
# Solution inspired by: https://stackoverflow.com/questions/18583214/calculate-angle-of-triangle-python
# Only peeve I have about this is: How can I prove that the line formed from Midpoint(M) to B(BM) is equivalent in magnitude to the line formed by CM
ans = int(round(degrees(acos((M**2+BC**2-M**2)/(2*M*BC)))))
print('{:d}{}'.format(ans, u'\N{DEGREE SIGN}'))
