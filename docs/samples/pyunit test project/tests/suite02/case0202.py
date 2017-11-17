'''
Created on Jul 20, 2016

@author: WAH
'''
import unittest
from aut.markdown_adapter import run_markdown


class TestMarkdownPy(unittest.TestCase):

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

    def test_non_marked_lines(self):
        ''' Non-marked lines should only get 'p' tags around all input
        '''
        result = run_markdown('this line has no special handling')
        self.assertEqual(result, 'this line has no special handling</p>')

    def test_em(self):
        ''' Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        result = run_markdown('*this should be wrapped in em tags*')
        self.assertEqual(result, '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        ''' Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        result = run_markdown('**this should be wrapped in strong tags**')
        self.assertEqual(result,'<p><strong>this should be wrapped in strong tags</strong></p>')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
