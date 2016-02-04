import time
from Controller.base import Base
from Model.Log import logger
from Views.index_view import repo

__author__ = 'kzhu'

class IndexPage(Base):
    def __init__(self,browser):
        # Base.__init__(self,browser)
        super(IndexPage,self).__init__(browser)

    def open(self,url):
        self.driver.get("http://"+url.rstrip())

    def login_as(self,username='',password=''):
        log = logger()
        driver = self.driver
        try:
            driver.by_id(repo['username']).clear()
            driver.by_id(repo['username']).send_keys(username)
            driver.by_id(repo['password']).clear()
            driver.by_id(repo['password']).send_keys(password)
            driver.by_xpath(repo['login_submit']).click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @login_as')
            log.log('[-] Error is '+str(e))

    def get_current_url(self):
        return super(IndexPage,self).get_current_url()


if __name__ == '__main__':
    index_instance  = IndexPage('chrome')
    index_instance.open('bbcerts.bbpd.io')
    index_instance.login_as()
    time.sleep(5)
    print index_instance.get_current_url()
    print index_instance.get_title()
    index_instance.quit()





