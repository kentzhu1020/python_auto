import  unittest
from Controller import inherit_controller
from Model.Config import const
from Model.Log import logger
from Model.Result import TestResult
from TestSuites import __init__

__author__ = 'kzhu'

class ModuleB(__init__):

    log = logger()
    @classmethod
    def setUpClass(cls):
        try:
            super(ModuleB, cls).setUpClass()
            cls.DRIVER.login_as(const['username'],const['password'])
        except Exception:
            cls.log.log('[+] Trying to start a webdriver but not the first one')
            cls.DRIVER = inherit_controller.Runner('chrome')
            cls.DRIVER.open(__init__.url)
            cls.DRIVER.login_as(const['username'],const['password'])

    @classmethod
    def tearDownClass(cls):
        super(ModuleB, cls).tearDownClass()

    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]


    def test_search(self):
        try:
            self.DRIVER.navigate_to_view_cert()
            self.assertEqual(self.DRIVER.get_title(),'View Certificate')
            self.DRIVER.search()
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

