import sys
import unittest
from xml.sax.handler import ContentHandler
from xml.sax import parseString

__unittest = True    # hide detailed traceback


class TestSuiteTemplate(unittest.TestSuite):
    
    def execute(self, verbosity=1, outputtype="default", output="", title="Test Report Title", description="Test Report Description"):
        """ execute the test suite using the assigned test runner """
        if outputtype == "xml":
            with open(output, 'wb') as output:
                testRunner = xmlrunner.XMLTestRunner(verbosity=verbosity, output=output)
                result = testRunner.run(self)
        elif outputtype == "html":
            from pats.pyunit import HTMLTestRunner
            with open(output, 'wb') as output:
                testRunner = HTMLTestRunner.HTMLTestRunner(stream=output, verbosity=verbosity, title=title, description=description)
                result = testRunner.run(self)
        else:
            testRunner = unittest.TextTestRunner(verbosity=verbosity)
            result = testRunner.run(self)
            
        return result


class TestCaseTemplate(unittest.TestCase):
    
    @classmethod
    def suite(cls):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(cls))
        return suite
    
    
    @classmethod
    def execute(cls, verbosity=2):
        unittest.main(verbosity=verbosity)
    
    
    def setUp(self):
        self.addCleanup(self._verifyErrors)
    
    
    def getCurrentTestName(self):
        return self._testMethodName
        
        
    def setCurrentTestDoc(self, testMethodDocString):
        self._testMethodDoc = testMethodDocString
        
        
    def getCurrentTestDoc(self):
        return self._testMethodDoc
    
    
    def perform(self, assertFun, *args ):
        '''continue the rest of test if assert failed
        '''
        if not hasattr(self, 'verificationErrors'):
            self.verificationErrors = []
        try: assertFun(*args)
        except AssertionError as e: self.verificationErrors.append(e)


    def _genErrorsMessage(self):
        """ format the error messages before it is used by test report
        """
        errMessage = ''
        totalErrors = len(self.verificationErrors)
        if totalErrors != 0:
            for err in self.verificationErrors:
                if errMessage == '':
                    errMessage = 'total %s error(s)\n\n%s'%(totalErrors, err.__str__())
                else:
                    errMessage = errMessage + '\n\n' + err.__str__()
        return errMessage

    def _verifyErrors(self):
        """ verify if the container is blank
        """
        if not hasattr(self, 'verificationErrors'):
            self.verificationErrors = []
        try:
            #result = not self.verificationErrors
            #self.assertTrue(result, self._genErrorsMessage())
            if self.verificationErrors:
                self.fail(self._genErrorsMessage())
        finally: 
            self.verificationErrors = []
            
            
            
    
    
    
    
    
            
            
    
        
            
    
            
    def verify_XML_is_well_formed(self, result, errMessage=None):
        """ verify the XML string is well-formed """
        try:
            parseString(result, ContentHandler())
            #print "XML string is well-formed"
        except Exception as e:
            #print "XML string is NOT well-formed! %s"%str(e)
            if errMessage:
                errMessage = "%s: %s" %(errMessage, str(e))
            else:
                errMessage = "XML string is NOT well-formed! %s"%e
            if HaltOnErr:
                raise AssertionError(errMessage)
            else:
                self.verificationErrors.append(errMessage)
    
    