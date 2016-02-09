"""
URL: http://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python
Your task is simply to count the total number of lowercase letters in a string.
"""
import numpy.testing.utils as Test
import re

def lowercase_count(strng):
    return len(re.findall('[a-z]', strng))

Test.assert_equal(lowercase_count("abc"), 3)
Test.assert_equal(lowercase_count("abcABC123"), 3)
Test.assert_equal(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
Test.assert_equal(lowercase_count(""), 0)
Test.assert_equal(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
Test.assert_equal(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)
