import time
from Controller.base import Base
from Model.Log import logger
from Views.request_cert_view import repo

__author__ = 'kzhu'

class RequestCertPage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)
        self.log = logger()

    def _input_csr(self,driver,csr):
        try:
            driver.find_element_by_id(repo['csr']).click()
            driver.find_element_by_id(repo['csr']).send_keys(csr)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @_input_csr')
            self.log.log('[-] Error is '+str(e))


    def _input_sans(self,driver,sans):
        try:
            driver.find_element_by_id(repo['sans']).click()
            driver.find_element_by_id(repo['sans']).send_keys(sans)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @_input_sans')
            self.log.log('[-] Error is '+str(e))


    def _input_comments(self,driver,comments):
        try:
            driver.find_element_by_id(repo['comment']).click()
            driver.find_element_by_id(repo['comment']).send_keys(comments)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @_input_comments')
            self.log.log('[-] Error is '+str(e))

    def _select_from_options_by_name(self,option_value,select_box):
        try:
            option_value = option_value.strip().lower()
            options = [item for item in select_box.find_elements_by_tag_name('option')]
            for element in options:
                element_value = element.get_attribute("value").strip().lower()
                element_text = element.text
                if element_value == option_value or element_text == option_value:
                    element.click()
        except Exception as er:
            self.log.log("Error occur @_select_from_options_by_name")
            self.log.log("Error is " +str(er))

    def _select_from_options_by_index(self,index,select_box):
        try:
            options = [item for item in select_box.find_elements_by_tag_name('option')]
            idx = index % len(options)
            options[idx].click()
            time.sleep(2)
        except Exception as er:
            self.log.log("Error occur @_select_from_options_by_index")
            self.log.log("Error is " +str(er))

    def _select_from_radio_by_name(self,selected,radio_button):
        try:
            option_value = str(selected).strip().lower()
            options = [item for item in radio_button.find_elements_by_name(repo['validity'])]
            for element in options:
                element_value = element.get_attribute("value").strip().lower()
                element_text = element.text
                if element_value == option_value or element_text == option_value:
                    element.click()
        except Exception as er:
            self.log.log("Error occur @_select_from_radio_by_name")
            self.log.log("Error is " +str(er))

    def _upload_csr(self,driver,filePath):
        try:
            driver.find_element_by_id(repo['upload']).send_keys(filePath)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @_upload_csr')
            self.log.log('[-] Error is '+str(e))


    def submit_form(self):
        driver = self.driver
        try:
            driver.by_id(repo['submit']).click()
        except Exception as er:
            self.log.log("Error occur @_select_from_options_by_index")
            self.log.log("Error is " +str(er))


    def input_data(self,ca_name,email_group,csr,server_platform_index,period,comments='test',sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self._select_from_options_by_name(ca_name,ca_select_box)
        self._select_from_options_by_name(email_group,mail_group_select_box)
        self._input_csr(driver,csr)
        self._input_sans(driver,sans)
        self._select_from_radio_by_name(period,period_radio)
        self._select_from_options_by_index(server_platform_index,server_type_select_box)
        self._input_comments(driver,comments)

    def input_data_by_upload(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments='test',sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self._select_from_options_by_name(ca_name,ca_select_box)
        self._select_from_options_by_name(email_group,mail_group_select_box)
        self._upload_csr(driver,csr_file_path)
        self._input_sans(driver,sans)
        self._select_from_radio_by_name(period,period_radio)
        self._select_from_options_by_index(server_platform_index,server_type_select_box)
        self._input_comments(driver,comments)



    def get_title(self):
        return super(RequestCertPage,self).get_title()