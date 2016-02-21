# based on https://github.com/ChristianECooper/CodeWars-Python-TestFramework/blob/master/Test.py

import sys
from datetime import datetime
import atexit

class Test(object):
    """
    Implements the test interface as described here:
    http://www.codewars.com/docs/python-test-reference-1
    """
    
    def __init__(self):
        self.totalFailures = 0
        self.totalSuccesses = 0
        
        self.currentBlockErrors = list()
        self.currentBlock = "Main tests"
        self.currentBlockFailures = 0
        self.currentBlockSuccesses = 0
        
        self.start = datetime.now()

    def describe(self, msg):
        print(msg)

    def it(self, msg):
        total = len(self.currentBlockErrors) + self.currentBlockSuccesses
        if total > 0:
            print("%s: %d/%d" % (self.currentBlock, self.currentBlockSuccesses, total))
            if total != self.currentBlockSuccesses:
                for err in self.currentBlockErrors:
                    print(err)
                print()
        
        self.currentBlock = msg
        self.currentBlockFailures = 0
        self.currentBlockSuccesses = 0
        self.currentBlockErrors.clear()

    def _assert(self, p, actual, expected, msg):
        if not p(expected, actual):
            self._error(msg, expected, actual)
        else:
            self._success()

    def assert_equals(self, actual, expected, msg="{} should be {}"):
        eq = lambda a, b: a == b
        self._assert(eq, actual, expected, msg)

    def assert_not_equals(self, actual, unexpected, msg="{} should be {}"):
        neq = lambda a, b: a != b
        self._assert(neq, actual, unexpected, msg)

    def expect_error(self, msg, fn):
        try:
            fn()
            self._error("Expected an error" if not msg else msg, None, None)
        except:
            self._success()

    def expect(self, b, msg="Unexpected result"):
        be = lambda a, e: b
        self._assert(be, b, None, msg)

    def _error(self, msg, expected, actual):
        self.currentBlockErrors.append("*** ERROR: {}".format(msg.format(expected, actual)))
        self.totalFailures += 1

    def _success(self):
        self.currentBlockSuccesses += 1
        self.totalSuccesses += 1

    def report(self):
        end = datetime.now()
        self.it("")
        print("\nTest run complete")
        print("Passed: {}".format(self.totalSuccesses))
        print("Failed: {}".format(self.totalFailures))
        print("Total:  {}".format(self.totalSuccesses + self.totalFailures))

        delta = end - self.start
        print("Process took {:,}ms to complete".format((delta.microseconds + 1000000 * delta.seconds) // 1000))
        if self.totalFailures == 0:
            print("Happy Days!")
        else:
            print("Better luck next time!")

test = Test()
atexit.register(test.report)