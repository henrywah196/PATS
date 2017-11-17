'''
Demo distinguishing test iterations using subtests

Created on Jul 20, 2016

@author: WAH
'''
import unittest

#@unittest.skip("")
class Case0302(unittest.TestCase):

    @classmethod
    def suite(cls):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(cls))
        return suite

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for param in range(0, 6):
            with self.subTest(param=param):
                self.assertEqual(param % 2, 0)


    def test_02_subTest(self):

        with self.subTest('verify assert equal'):
            current = 2
            expected = 1
            self.assertEqual(current, expected, "current is not expected")

        with self.subTest("verify is True"):
            result = False
            self.assertTrue(result, "result is not expected")

        for i in range(0, 6):
            msg = "verify if number is even: %s"%i
            with self.subTest(msg):
                self.assertEqual(i % 2, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
