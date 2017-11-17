'''
Created on Jul 20, 2016

@author: WAH
'''
import unittest


class Case0101(unittest.TestCase):

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

    def test_01(self):
        print("execute test '%s.%s'"%(self.__class__.__name__, self._testMethodName))

    def test_02(self):
        print("execute test '%s.%s'"%(self.__class__.__name__, self._testMethodName))

    def test_03(self):
        print("execute test '%s.%s'"%(self.__class__.__name__, self._testMethodName))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()