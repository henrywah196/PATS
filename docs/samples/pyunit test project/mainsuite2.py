'''
Created on Jul 20, 2016

@author: WAH
'''
import os
import unittest
from pats.pyunit.testtemplate import TestSuiteTemplate


if __name__ == "__main__":
    main_suite = TestSuiteTemplate()

    tests = unittest.TestLoader().discover(start_dir='tests', pattern='case*.py')

    main_suite.addTest(tests)
    
    filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report" + '.html')

    main_suite.execute(verbosity=2, outputtype="html", output=filePath)

