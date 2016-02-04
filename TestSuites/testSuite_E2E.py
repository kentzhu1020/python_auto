import os
import  unittest
from Controller import inherit_controller
from Model.Log import logger
from Model.Result import TestResult
from TestSuites import __init__


__author__ = 'kzhu'


class EndToEndModule(__init__):

    log = logger()


    @classmethod
    def setUpClass(cls):
        try:
            super(EndToEndModule, cls).setUpClass()
            cls.DRIVER.login_as('kzhu','Black@1')

        except Exception:
            cls.log.log('[+] Trying to start a webdriver but not the first one')
            cls.DRIVER = inherit_controller.Runner('chrome')
            cls.DRIVER.open(__init__.url)
            cls.DRIVER.login_as('kzhu','Black@1')

    @classmethod
    def tearDownClass(cls):
        super(EndToEndModule, cls).tearDownClass()
    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]


    def test_navigation(self):
        try:
            self.DRIVER.navigate_to_help()
            self.assertEqual(self.DRIVER.get_title(),'Help Page')
            self.DRIVER.navigate_to_home()
            self.assertEqual(self.DRIVER.get_title(),'Home Page')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

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

    def test_create_group(self):
        try:
            self.DRIVER.navigate_to_notification_group()
            self.assertEqual(self.DRIVER.get_title(),'Notification Group')
            group_name = self.DRIVER.get_group_table_value(1,'Creator')
            self.assertEqual(group_name,'Kent Zhu')
            self.DRIVER.show_tooltip()
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_request_cert(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            self.DRIVER.navigate_to_sub_menu('SSL Multi Domain Certificates')
            self.DRIVER.input_data_by_upload('Comodo','Security',BASE_DIR+'/Data/server.csr',42,3,'testsasasasasasasasasasasa','abc.test.com')
            self.DRIVER.navigate_to_help()
            self.assertEqual(self.DRIVER.get_title(),'Help Page')
            self.DRIVER.navigate_to_home()
            self.assertEqual(self.DRIVER.get_title(),'Home Page')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
