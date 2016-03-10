import time
from Controller.base import Base
from Model.Log import logger
from Views.group_view import repo

__author__ = 'kzhu'

class GroupPage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)
        self.log = logger()

    def __input_group_name(self,driver,group_name):
        driver.find_element_by_id(repo['group_name']).send_keys(group_name)

    def __input_group_email_addrss(self,driver,group_email_address):
        driver.find_element_by_id(repo['group_email_address']).send_keys(group_email_address)

    def __input_group_contact_phone(self,driver,phone_number):
        driver.find_element_by_id(repo['group_contract_phone_number']).send_keys(phone_number)

    def __type_submit(self,driver):
        driver.by_id(repo['submit']).click()

    def __type_cancel(self,driver):
        driver.by_xpath(repo['cancel']).click()


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

    def get_last_table_value(self,header_name):
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
            cell_value = table_body[total_row_number].find_elements_by_tag_name('td')[idx].text.encode('utf8')
            return cell_value
        except Exception as er:
            self.log.log('[-] Error occur @get_last_table_value')
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

    def __new_a_group(self,driver,group_name,group_email_address,contact_number):
        try:
            driver.by_link_text(repo['new_group']).click()
            time.sleep(2)
            driver.by_id(repo['group_name']).send_keys(group_name)
            driver.by_id(repo['group_email_address']).send_keys(group_email_address)
            driver.by_id(repo['group_contract_phone_number']).send_keys(contact_number)
            time.sleep(2)
        except Exception as er:
            self.log.log('[-] Error occur @__new_a_group')
            self.log.log('[-] Error is '+str(er))

    def cancel_new_a_group(self,group_name,group_email_address,contact_number):
        try:
            driver = self.driver
            self.__new_a_group(driver,group_name,group_email_address,contact_number)
            self.__type_cancel(driver)
            time.sleep(2)
        except Exception as er:
            self.log.log('[-] Error occur @cancel_new_a_group')
            self.log.log('[-] Error is '+str(er))


    def submit_a_group(self,group_name,group_email_address,contact_number):
        try:
            driver = self.driver
            self.__new_a_group(driver,group_name,group_email_address,contact_number)
            self.__type_submit(driver)
            time.sleep(2)
        except Exception as er:
            self.log.log('[-] Error occur @submit_a_group')
            self.log.log('[-] Error is '+str(er))


    def get_alert_message(self):
        try:
            driver = self.driver
            alert = ''
            time.sleep(5)
            alerts = driver.find_elements_by_xpath(repo['alert'])
            if len(alerts) == 1:
                return alerts[0].text
            else:
                for alert_item in alerts:
                    alert = alert+alert_item.text
                return alert
        except Exception as er:
            self.log.log('[-] Error occur @get_alert_message')
            self.log.log('[-] Error is '+str(er))



    def get_title(self):
        return super(GroupPage,self).get_title()

