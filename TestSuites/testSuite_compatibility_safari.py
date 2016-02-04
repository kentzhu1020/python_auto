import  unittest
from Controller import inherit_controller
from Model.Result import TestResult


__author__ = 'kzhu'
class CompatibilitySafari(unittest.TestCase):

    SAFARI = inherit_controller.Runner('safari')

    @classmethod
    def setUpClass(cls):
        cls.SAFARI.open('bbcerts.bbpd.io')
        return cls.SAFARI

    @classmethod
    def tearDownClass(cls):
        cls.SAFARI.quit('safari')


    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]

    def test_login(self):
        try:
            self.SAFARI.login_as('kzhu','Black@1')
            self.assertEqual(self.SAFARI.get_title(),'Home Page')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))


    def test_create_group(self):
        try:
            self.SAFARI.login_as('kzhu','Black@1')
            self.SAFARI.navigate_to_notification_group()
            self.assertEqual(self.SAFARI.get_title(),'Notification Group')
            group_name = self.SAFARI.get_group_table_value(1,'Creator')
            self.assertEqual(group_name,'Kent Zhu')
            self.SAFARI.show_tooltip_safari()
            self.SAFARI.logout()
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()