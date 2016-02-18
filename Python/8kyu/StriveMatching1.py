"""
URL: http://www.codewars.com/kata/strive-matching-number-1/train/python

"""
from CodeWarsFW import test

def match(candidate, job):
    cPrice = candidate["min_salary"]
    jPrice = job["max_salary"]
    if (cPrice is None) or (jPrice is None):
        raise Exception("Error")
    
    wiggle = cPrice * 0.1
    return cPrice <= (jPrice + wiggle)

test.describe("Basic tests")
candidate1 = { "min_salary": 120000 }
candidate2 = { "min_salary": 190000 }
job1 = { "max_salary": 130000 }
job2 = { "max_salary": 80000 }
job3 = { "max_salary": 171000 }

test.it("should detect valid matches")
test.assert_equals(match(candidate1, job1), True)
test.assert_equals(match(candidate1, job3), True)
test.assert_equals(match(candidate2, job3), True)

test.it("should detect invalid matches")
test.assert_equals(match(candidate1, job2), False)
test.assert_equals(match(candidate2, job1), False)
test.assert_equals(match(candidate2, job2), False)

test.it("should throw when a candidate has no min_salary")
test.expect_error("Should throw error", lambda a: match({}, job2))

test.it("should throw when a job has no max_salary")
test.expect_error("Should throw error", lambda a: match(candidate1, {}))