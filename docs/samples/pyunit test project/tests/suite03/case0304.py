'''
Demo continue the reset of tests after assert failed

Created on Jul 20, 2016

@author: WAH
'''
from pats.pyunit.testtemplate import TestCaseTemplate
from pats.delayedAssert import expect, assert_expectations


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

    def test_01(self):

        step = "verify current equals to expected"
        current = 1
        expected = 2
        err_message = "%s => failed"%step
        self.perform(self.assertEqual, current, expected, err_message)

        step = "verify result is expected"
        result = False
        err_message = "%s => failed"%step
        self.perform(self.assertTrue, result, err_message)

        step = "verify items in two lists are equal"
        current = [1, 3, 5, "A", "google"]
        expected = ["google", 5, "A", 1, 3]
        err_message = "%s => failed"%step
        self.perform(self.assertCountEqual, current, expected, err_message)

        current = [1, 3, 5, "koodo", "A"]
        self.perform(self.assertCountEqual, current, expected, err_message)

        step = "verify result contains expected item"
        result = "Hello world python"
        target = "World"
        err_message = "%s => failed"%step
        self.perform(self.assertIn, target, result, err_message)

        #self._verifyErrors()


    def test_02(self):

        step = "verify current equals to expected"
        current = 1
        expected = 2
        err_message = "%s => failed"%step
        expect(current == expected, err_message)

        step = "verify result is expected"
        result = False
        err_message = "%s => failed"%step
        expect(result is True, err_message)

        step = "verify items in two lists are equal"
        current = [1, 3, 5, "A", "google"]
        expected = ["google", 5, "A", 1, 3]
        err_message = "%s => failed"%step
        expect(current == expected, err_message)

        current = [1, 3, 5, "koodo", "A"]
        expect(current == expected, err_message)

        step = "verify result contains expected item"
        result = "Hello world python"
        target = "World"
        err_message = "%s => failed"%step
        expect(target in result, err_message)

        assert_expectations()


if __name__ == "__main__":
    Case0304.execute()
