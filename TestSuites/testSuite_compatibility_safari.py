import os
import  unittest
from Controller import inherit_controller
from Model.Config import const
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
            self.SAFARI.login_as(const['username'],const['password'])
            self.assertEqual(self.SAFARI.get_title(),'Home Page')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))


    def test_create_group(self):
        try:
            self.SAFARI.login_as(const['username'],const['password'])
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

    def test_generate_csr(self):
        try:
            self.SAFARI.login_as(const['username'],const['password'])
            self.SAFARI.navigate_to_sub_links('SSL Plus Certificate')
            self.SAFARI.type_csr_generation_link()
            self.assertEqual(self.SAFARI.get_title(),'CSR Generation')
            self.SAFARI.input_data_csr('testserver.blackboard.com','Blackboard','aaaa','aaa of Columbia','Cloud aa',3,1,sans='test.test.com')
            self.SAFARI.click_generate()
            self.SAFARI.return_to_request_cert()
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_request_cert_input_csr(self):
        csr = """-----BEGIN CERTIFICATE REQUEST-----
MIIC+jCCAeICAQAwgbQxCzAJBgNVBAYTAlVTMREwDwYDVQQIEwhWaXJnaW5pYTEP
MA0GA1UEBxMGUmVzdG9uMR0wGwYDVQQKExRCbGFja2JvYXJkIEluYy4gVGVzdDER
MA8GA1UECxMIU2VjdXJpdHkxIjAgBgNVBAMTGXRlc3RzZXJ2ZXIuYmxhY2tib2Fy
ZC5jb20xKzApBgkqhkiG9w0BCQEWHG1pY2hhZWwucGVlbGVAYmxhY2tib2FyZC5j
b20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDF3ZcwyNNM/Ldl+AO4
6ZzjEy+OxmnxHdyOVOpXtCA4RXiJ/wH6FRQ/Rnk6zkfwgycg2XHK28yNpxauuK9S
xitWRIRLQyJBYkXN1SLTGyANregvQFwLhdU+zgYPklukVjQSrxt1Yt8r3Ek6YyjL
ylkdpI8/txiw9Nk7yzSfTarlTkaOTRtI0bV5AujNhVW+rHJ301GoB7DCzPeJ7+7H
C0MsG/Dd9L4M6dLJoF9y0lqWHBCTq/ueO7Z5UQMopo29GfwCmhB9Bh4GggqqrDSP
j2ekOFmAsXILkzeqLJxk8/c0wwtNgFit74trD6bCGXwjpYKj8bN2KbfY1tjyeXBO
4YHpAgMBAAGgADANBgkqhkiG9w0BAQUFAAOCAQEAtx5j68iq0j19I0PP//4vVMEo
24hoPSYxecm/mb+0A1rAB183YS5aKLHYPO+x6NU6Kcp9bHg8+LUambh8nRmaqgzd
NpsHCbC7b2QLWTBXT63JjFfDroLqqE2TLoj36Iz+5Z3tm8hkl/YaPyNqdmhuOaZj
9Hhaj6tR2DSwp4ZDQWa22GzapZwXymCdQPgkJOMVRQxP1035vEPZr10AEQ3Fj/c9
G0NCzTzCOpuZbadGs/YWDvRYCp4FrnGBBETANKLNhSYmfjOPsvEmzcp8Rz6uBHYM
aXCumZwqTwOG1GLsJ14KZUDRw7qz/bTAixH+aqwk12a7milOnIk12iZu5bdQzw==
-----END CERTIFICATE REQUEST-----
        """
        try:
            self.SAFARI.login_as(const['username'],const['password'])
            self.SAFARI.navigate_to_sub_links('SSL Multi Domain Certificates')
            self.SAFARI.input_data_SSLMDC('Comodo','Security',csr,42,3,'testsasasasasasasasasasasa','abc.test.com')
            self.SAFARI.navigate_to_help()
            self.assertEqual(self.SAFARI.get_title(),'Help Page')
            self.SAFARI.navigate_to_home()
            self.assertEqual(self.SAFARI.get_title(),'Home Page')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def test_request_cert_by_uploading(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            self.SAFARI.login_as(const['username'],const['password'])
            self.SAFARI.navigate_to_sub_links('SSL Multi Domain Certificates')
            self.SAFARI.input_data_by_upload_SSLMDC('Comodo','Security',BASE_DIR+'/Data/server.csr',42,3,'testsasasasasasasasasasasa','abc.test.com')
            self.SAFARI.navigate_to_help()
            self.assertEqual(self.SAFARI.get_title(),'Help Page')
            self.SAFARI.navigate_to_home()
            self.assertEqual(self.SAFARI.get_title(),'Home Page')
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()