"""
URL: http://www.codewars.com/kata/56269eb78ad2e4ced1000013
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
"""

import numpy.testing.utils as test

def isPalindrome(val):
    s = str(val)
    hl = int(len(s) / 2)
    return s[:hl] == s[-hl:][::-1]

def next_pal(val):
    while True:
        val += 1
        if isPalindrome(val):
            return val
    return 0

test.assert_equal(next_pal(11), 22)
test.assert_equal(next_pal(188), 191)
test.assert_equal(next_pal(191), 202)
test.assert_equal(next_pal(2541), 2552)