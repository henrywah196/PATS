'''
Created on Jul 20, 2016

@author: WAH
'''
import unittest
from aut.unnecessary_math import multiply


class TestUM(unittest.TestCase):

    @classmethod
    def suite(cls):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(cls))
        return suite

    @classmethod
    def setUpClass(cls):
        print("test setup for '%s'"%cls.__name__)

    @classmethod
    def tearDownClass(cls):
        print("test clean up for '%s'"%cls.__name__)

    def setUp(self):
        print("test setup for '%s.%s'"%(self.__class__.__name__, self._testMethodName))

    def tearDown(self):
        print("test clean up for '%s.%s'"%(self.__class__.__name__, self._testMethodName))

    def test_numbers_3_4(self):
        ''' verify 3 x 4 = 12
        '''
        self.assertEqual( multiply(3,4), 12)

    def test_strings_a_3(self):
        ''' verify a multiply 3 times
        '''
        self.assertEqual( multiply('a',3), 'aaa')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
