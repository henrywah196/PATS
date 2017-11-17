'''
Demo data driven test using ddt module

Created on Jul 20, 2016

@author: WAH
'''
from pats.pyunit.testtemplate import TestCaseTemplate
from ddt import ddt, data


def get_testing_data():
    ''' return a list of test data
    '''
    class Object(object):
        pass
    test_data = []
    for i in range(0, 6):
        test_obj = Object()
        setattr(test_obj, 'value', i)
        test_data.append(test_obj)
    return test_data


@ddt
class Case0304(TestCaseTemplate):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        super(Case0304, self).setUp()

    def tearDown(self):
        pass

    @data(*get_testing_data())
    def test_01(self, test_data):

        self.setCurrentTestDoc("verify if number {0} is even".format(test_data.value))
        self.assertEqual(test_data.value % 2, 0)


if __name__ == "__main__":
    Case0304.execute()
