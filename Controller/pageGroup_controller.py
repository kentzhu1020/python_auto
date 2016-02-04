import time
from Controller.base import Base
from Model.Log import logger
from Views.group_view import repo

__author__ = 'kzhu'

class GroupPage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)
        self.log = logger()

    def get_group_table_value(self,row_num,header_name):
        driver = self.driver
        try:
            idx = 0
            table_body = driver.by_id(repo['view_group_table']).find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
            total_row_number = len(table_body)-1
            headers = table_body[0].find_elements_by_tag_name('th')
            for i in range(0,len(headers)):
                if header_name == headers[i].text:
                    idx = i
                    time.sleep(1)
                    break
            if row_num <=0 or row_num>total_row_number:
                cell_value = ''
                self.log.log('[-] Error occur @get_group_table_value')
                self.log.log('[-] Error is row number is illegitimate')
            else:
                cell_value = table_body[row_num].find_elements_by_tag_name('td')[idx].text.encode('utf8')
            return cell_value
        except Exception as er:
            self.log.log('[-] Error occur @get_group_table_value')
            self.log.log('[-] Error is '+str(er))


    def show_tooltip(self):
        driver = self.driver
        creator = driver.by_xpath(repo['creator_tooltip'])
        self.move_to_element(driver,creator)
        time.sleep(2)

    def show_tooltip_safari(self):
        driver = self.driver
        target = driver.by_xpath(repo['creator_tooltip'])
        self.move_to_element_by_js(driver,target)
        time.sleep(2)



    def get_title(self):
        return super(GroupPage,self).get_title()

