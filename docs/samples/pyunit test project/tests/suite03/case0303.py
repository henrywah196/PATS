'''
Demo unittest assert

Created on Jul 20, 2016

@author: WAH
'''
import unittest


class Case0303(unittest.TestCase):

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

    def test_01(self):
        '''verify current equals to expected
        '''
        current = 1
        expected = 2
        self.assertEqual(current, expected, "current is not expected")

    def test_02(self):
        '''verify result is expected
        '''
        result = False
        self.assertTrue(result, "result is not expected")

    def test_03(self):
        '''verify items in two lists are equal
        '''
        current = [1, 3, 5, "A", "google"]
        expected = ["google", 5, "A", 1, 3]
        self.assertCountEqual(current, expected, "current items is not expected")

        current = [1, 3, 5, "koodo", "A"]
        self.assertCountEqual(current, expected, "current items is not expected")


    def test_04(self):
        ''' verify result contains expected item
        '''
        result = "Hello world python"
        target = "World"
        self.assertIn(target, result, "result has no expected item")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
