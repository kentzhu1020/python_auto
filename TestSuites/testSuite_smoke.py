import csv
import os
import  unittest
from Controller import inherit_controller
from Model.Log import logger
from Model.Result import TestResult
from Model.Utility import DBConnection
from TestSuites import __init__

__author__ = 'kzhu'

class SmokeTestSuite(__init__):

    log = logger()

    @classmethod
    def setUpClass(cls):
        try:
            super(SmokeTestSuite, cls).setUpClass()
        except Exception:
            cls.log.log('[+] Trying to start a webdriver but not the first one')
            cls.DRIVER = inherit_controller.Runner('chrome')
            cls.DRIVER.open(__init__.url)

    @classmethod
    def tearDownClass(cls):
        super(SmokeTestSuite, cls).tearDownClass()

    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]

    def tearDown(self):
        pass

    def test_login(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db = DBConnection()
        with open(BASE_DIR+'/Data/login_data.csv') as configfile:
            reader = csv.DictReader(configfile)
            for row in reader:
                username = row['username']
                password = row['password']
                try:
                    self.DRIVER.login_as(username,password)
                    self.assertEqual(self.DRIVER.get_title(),'Home Page',
                                    'Login failed with username '+username+' and password '+password+'! Please check')
                    self.assertEqual(db.get_user_email_address(username),self.DRIVER.get_user_email_address(),
                                     'User logged in but with different session')
                    self.DRIVER.logout()
                    TestResult().addSuccess(self.suite_name,0,self.case_name+'_'+row['#'],'')
                except AssertionError as ae:
                    TestResult().addFail(self.suite_name,1,self.case_name+'_'+row['#'],str(ae))
                    self.DRIVER.take_screenshot(self.case_name+'_'+row['#']+'.png',BASE_DIR+'/Results')
                except Exception as e:
                    TestResult().addError(self.suite_name,2,self.case_name+'_'+row['#'],str(e))

    def test_search(self):
        try:
            self.DRIVER.login_as('kzhu','Black@1')
            self.DRIVER.navigate_to_view_cert()
            self.assertEqual(self.DRIVER.get_title(),'View Certificate')
            self.DRIVER.search()
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))


if __name__ == "__main__":
    unittest.main()




