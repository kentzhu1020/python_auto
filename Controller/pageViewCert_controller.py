import time
from Controller.base import Base
from Model.Log import logger
from Views.view_certs_view import repo

__author__ = 'kzhu'

class ViewCertPage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)
        self.log = logger()

    def search(self):
        driver = self.driver
        try:
            driver.by_xpath(repo['search']).send_keys('test')
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @search')
            self.log.log('[-] Error is '+str(e))

    def get_certs_table_value(self,header_name):
        driver = self.driver
        try:
            idx = 0
            headers = driver.by_id(repo['view_certs_table']).find_element_by_tag_name('thead').find_element_by_tag_name('tr').find_elements_by_tag_name('th')
            for i in range(0,len(headers)):
                if header_name == headers[i].text:
                    idx = i
                    time.sleep(1)
                    break
            table_bodys = driver.by_id(repo['view_certs_table']).find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
            cell_value = table_bodys[0].find_elements_by_tag_name('td')[idx].text.encode('utf8')
            return cell_value
        except Exception as er:
            self.log.log('[-] Error occur @get_certs_table_value')
            self.log.log('[-] Error is '+str(er))


    def get_title(self):
        return super(ViewCertPage,self).get_title()