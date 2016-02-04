from Controller.pageGroup_controller import GroupPage
from Controller.pageIndex_controller import IndexPage
from Controller.pageHome_controller import HomePage
from Controller.pageViewCert_controller import ViewCertPage
from Controller.pagesRequestCert_controller import RequestCertPage

__author__ = 'kzhu'

class Runner(IndexPage,HomePage,GroupPage,ViewCertPage,RequestCertPage):
    def __init__(self,browser):
        super(Runner,self).__init__(browser)


# if __name__ == '__main__':
#     user = Runner('chrome')
#     user.open('bbcerts.bbpd.io')
#     user.login_as()
#     time.sleep(5)
#     print user.get_current_url()
#     print user.get_title()
#     user.quit()