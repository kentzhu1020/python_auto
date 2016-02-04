import  unittest
from Controller import inherit_controller
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
            cls.DRIVER.login_as('kzhu','Black@1')
        except Exception:
            cls.log.log('[+] Trying to start a webdriver but not the first one')
            cls.DRIVER = inherit_controller.Runner('chrome')
            cls.DRIVER.open(__init__.url)
            cls.DRIVER.login_as('kzhu','Black@1')

    @classmethod
    def tearDownClass(cls):
        super(ModuleB, cls).tearDownClass()

    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]

    def test_navigation(self):

        csr = """-----BEGIN CERTIFICATE REQUEST-----
MIIC3zCCAccCAQAwgZkxHTAbBgNVBAoTFERvbWVueS5wbCBzcC4geiBvLm8uMQsw
CQYDVQQLEwJJVDEdMBsGCSqGSIb3DQEJARYOaW5mb0Bkb21lbnkucGwxFDASBgNV
BAgTC21hbG9wb2xza2llMQ8wDQYDVQQHEwZLcmFrb3cxCzAJBgNVBAYTAlBMMRgw
FgYDVQQDEw9kb21lbnktdGVzdC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQCZNgpyFKjKwxCTYO71wEXo0W/GC3uJwPmRM99RgxU36qCCAal7/ejv
tGdNdyL/I4GRBGzHeZ892a7MvADVVWIva3wgnLgIf2KmS6T1DuTafTHW3idkEh8K
c4RG8C/nyFAbC4/o6UX0rjoLy1UccnTc6N+tjQymlchNaKYN/de0YVhqoZXuPHGj
Y93xZR6/MuI/6niQGf+MFRX8PV0dnZosxXuWBnIU+COayT7Vm7MleGgvwE+AqCwW
T44MMkkXBxOQtLwVQi6sVrKzox0rPhOAJgWqnF24tzP9YpxRZspLDgBT1SkpLA63
uwnA71F/vGqqQkW4JCUyyEskC6xMssJbAgMBAAGgADANBgkqhkiG9w0BAQQFAAOC
AQEAQFT5a7x10DKCPG8k1d1gAx1w++vzK08e/ldURpLuf/CdfVfTgliRr9xiopCg
ESfdkHdRKZL8/4WcZxBXZqkg487hHVm6Wj4O80bKKki1ng3DlXHvLiPwHHLt0mnj
JVIy/P6G5mamf0lG5hs+PQK7K6ZRGERXAWmQGQdR6ciDWoA5n5SaXC3mMY+KTbin
HCcpd2FXrKSJYjnHq8HJreETNttE5gJX/L1KGjcx3GVJfZ7vetVX+B7rLwdkjHOD
3phnKZWRJFfcGxqlVuVQtKMUyXRatHdoigZPsqIG3aha4w+lCBzcg7nW18Krr5QA
b9yN0VKDCoY7xPZjlwu0HhfF0A==
-----END CERTIFICATE REQUEST-----"""
        try:
            self.DRIVER.navigate_to_sub_menu('SSL Multi Domain Certificates')
            self.DRIVER.input_data('Comodo','Security',csr,42,3,'testsasasasasasasasasasasa','abc.test.com')
            self.DRIVER.navigate_to_help()
            self.assertEqual(self.DRIVER.get_title(),'Help Page')
            self.DRIVER.navigate_to_home()
            self.assertEqual(self.DRIVER.get_title(),'Home Page')
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

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

