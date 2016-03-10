import os
import  unittest
import time
from Controller import inherit_controller
from Model.Config import const
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
            cls.DRIVER.login_as(const['username'],const['password'])

        except Exception:
            cls.log.log('[+] Trying to start a webdriver but not the first one')
            cls.DRIVER = inherit_controller.Runner('chrome')
            cls.DRIVER.open(__init__.url)
            cls.DRIVER.login_as(const['username'],const['password'])

    @classmethod
    def tearDownClass(cls):
        super(EndToEndModule, cls).tearDownClass()

    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]
        today = time.strftime("%Y%m%d%H%M%S")
        self.group_name = 'A_TEST_'+today
        self.group_email_address = 'test@test'+today+'.com'


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
            self.DRIVER.input_data_by_upload_SSLMDC('Comodo','Security',BASE_DIR+'/Data/server.csr',42,3,'testsasasasasasasasasasasa','abc.test.com')
            self.DRIVER.navigate_to_help()
            self.assertEqual(self.DRIVER.get_title(),'Help Page')
            self.DRIVER.navigate_to_home()
            self.assertEqual(self.DRIVER.get_title(),'Home Page')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_cancel_button(self):
        try:
            self.DRIVER.navigate_to_notification_group()
            self.assertEqual(self.DRIVER.get_title(),'Notification Group')
            self.DRIVER.cancel_new_a_group('A_TEST_001','test@test.com','+41421234567')
            self.assertEqual(self.DRIVER.get_title(),'Notification Group')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_new_group(self):
        try:
            self.DRIVER.navigate_to_notification_group()
            self.assertEqual(self.DRIVER.get_title(),'Notification Group')
            self.DRIVER.submit_a_group(self.group_name,self.group_email_address,'+13524900000')
            self.assertEqual(self.DRIVER.get_title(),'Notification Group')
            self.assertEqual(self.DRIVER.get_last_table_value('Group Name'),self.group_name)
            self.assertEqual(self.DRIVER.get_last_table_value('Group E-mail Address'),self.group_email_address)
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_validate_phone_number(self):
        try:
            self.DRIVER.navigate_to_notification_group()
            self.assertEqual(self.DRIVER.get_title(),'Notification Group')
            self.DRIVER.submit_a_group(self.group_name,self.group_email_address,'+uuuu44433')
            self.assertEqual(self.DRIVER.get_alert_message(),'Enter a valid phone number.')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_generate_csr(self):
        try:
            self.DRIVER.navigate_to_sub_menu('SSL Plus Certificate')
            self.DRIVER.type_csr_generation_link()
            self.assertEqual(self.DRIVER.get_title(),'CSR Generation')
            self.DRIVER.input_data_csr('testserver.blackboard.com','Blackboard','aaaa','aaa of Columbia','Cloud aa',3,1,sans='test.test.com')
            self.DRIVER.click_generate()
            self.DRIVER.return_to_request_cert()
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_request_cert_by_uploading(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            self.DRIVER.login_as('kzhu','Black@2')
            self.DRIVER.navigate_to_sub_links('SSL Multi Domain Certificates')
            self.DRIVER.input_data_by_upload_SSLMDC_safari('Comodo','Security',BASE_DIR+'/Data/server.csr',42,3,'testsasasasasasasasasasasa','abc.test.com')
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
