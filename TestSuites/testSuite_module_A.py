import  unittest
from Controller import inherit_controller


__author__ = 'kzhu'
class ModuleA(unittest.TestCase):

    instance = inherit_controller.Runner('chrome')

    @classmethod
    def setUpClass(cls):
        return cls.instance

    @classmethod
    def tearDownClass(cls):
        cls.instance.quit()


    def setUp(self):
        self.url = 'bbcerts.bbpd.io'
        self.instance.open(self.url)
        self.instance.login_as('kzhu','Black@1')
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]

    def test_login(self):
        self.assertEqual(self.instance.get_title(),'Home Page')

    def test_navigation(self):
        self.instance.navigate_to_help()
        self.assertEqual(self.instance.get_title(),'Help Page')
        self.instance.navigate_to_home()
        self.assertEqual(self.instance.get_title(),'Home Page')

    def test_search(self):
        self.instance.navigate_to_view_cert()
        self.assertEqual(self.instance.get_title(),'View Certificat')
        self.instance.search()


    def tearDown(self):
        self.instance.clear_cookies()




if __name__ == "__main__":
    unittest.main()
