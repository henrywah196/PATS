'''
Created on Jul 20, 2016

@author: WAH
'''
import unittest
import xmlrunner
from HtmlTestRunner import HTMLTestRunner
from pats.pyunit.testtemplate import TestSuiteTemplate

# import test cases
from tests.suite01 import suite01
from tests.suite02 import suite02
from tests.suite03 import suite03


def suite():

    # prepare test suites
    suite1 = suite01.suite()
    suite2 = suite02.suite()
    suite3 = suite03.suite()

    suite = unittest.TestSuite()
    suite.addTests((suite1, suite2, suite3))
    return suite

if __name__ == "__main__":
    testRunner = unittest.TextTestRunner(verbosity=2)
    #testRunner = xmlrunner.XMLTestRunner(output='example_suite')
    #testRunner = HTMLTestRunner(output='example_suite')

    tests = unittest.TestLoader().discover(start_dir='tests', pattern='case*.py')

    result = testRunner.run(tests)

    print(result)

