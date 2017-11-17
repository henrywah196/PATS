'''
unittest skip test demo

Created on Jul 20, 2016

@author: WAH
'''
import unittest

IMPLEMENTED = False
PLATFORM = "win"
CONDITION = False

class Case0301(unittest.TestCase):

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

        if self._testMethodName == "test_04":
            if not CONDITION:
                self.skipTest("test condition for '%s' is not ready yet"%self._testMethodName)

    def tearDown(self):
        print("test clean up for '%s.%s'"%(self.__class__.__name__, self._testMethodName))

    @unittest.skip("demonstrating skipping")
    def test_01_skip(self):
        '''demo unittest.skip()
        '''
        self.fail("shouldn't happen")

    @unittest.skipIf(IMPLEMENTED is False, "not yet implemented")
    def test_02_skipIf(self):
        '''demo unittest.skipIf()
        '''
        self.fail("shouldn't happen")

    @unittest.skipUnless( PLATFORM == "linux", "Only test under linux")
    def test_03_skipUnless(self):
        '''demo unittest.skipUnless()
        '''
        self.fail("shouldn't happen")

    def test_04(self):
        '''demo self.skipTest()
        '''
        result = True
        self.assertTrue(result, "result is not expected")

    @unittest.expectedFailure
    def test_05_expectedFailure_01(self):
        '''demo unexpected success
        '''
        result = True
        self.assertTrue(result, "result is not expected")

    @unittest.expectedFailure
    def test_05_expectedFailure_02(self):
        '''demo unittest.expectedFailure
        '''
        result = False
        self.assertTrue(result, "result is expected")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)
