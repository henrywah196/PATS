'''
Created on Jul 20, 2016

@author: WAH
'''
import unittest


def suite():
    ''' prepare test suites
    '''

    return unittest.TestLoader().discover(start_dir='.', pattern='case*.py')


if __name__ == "__main__":
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(suite())
