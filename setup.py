#--------------------------------------------------------------------------------------
# Setup:    setup PATS, install required modules 
# 
#
#
# Author:        Henry Wang
# Created:       Aug 08, 2015
#--------------------------------------------------------------------------------------
import sys, os, shutil, site, pip
from setuptools.command import easy_install

def setup():

    print("\nCheck python version ...")
    if sys.version_info[0] < 3: 
        raise Exception("PATS must be installed and used under Python 3.x")
    
    print("\nSetup PATS(Python Auto Test Suite) at '%s' ...\n"%(os.path.dirname(os.path.abspath(__file__))))
    #easy_install.main(['nose', 'nose-html', 'ddt', 'selenium', 'pywinauto', 'requests', 'pil'])
    pip.main(['install', 'unittest-xml-reporting'])    # https://github.com/xmlrunner/unittest-xml-reporting
    print("")
    pip.main(['install', 'html-testRunner'])    # https://github.com/oldani/HtmlTestRunner
    print("")
    pip.main(['install', 'ddt'])    # http://ddt.readthedocs.org/
    

    """
	print "\nModify ddt module ...\n"
    reload(site)
    import ddt
    dst = os.path.join(os.path.dirname(ddt.__file__), "ddt.py")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "setup", "ddt.py")
    print "replace: %s"%dst
    print "with: %s"%src
    shutil.copyfile(src, dst)
	"""

    print("\nPrepare .pth file ... \n")
    fileName = os.path.basename(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))) + ".pth"
    fileFullName = os.path.join(site.getsitepackages()[1], fileName)
    print("... '%s' is created"%fileFullName)
    file = open(fileFullName, 'w')
    file.write(os.path.dirname(os.path.abspath(__file__)))
    file.close()


if __name__ == "__main__":
    setup()





