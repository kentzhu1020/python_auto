import subprocess
import time
from Controller.base import Base
from Model.Log import logger
from Views.request_cert_view import repo

__author__ = 'kzhu'

class RequestCertPage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)
        self.log = logger()

    def __input_csr(self,driver,csr):
        try:
            driver.find_element_by_id(repo['csr']).click()
            driver.find_element_by_id(repo['csr']).send_keys(csr)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @__input_csr')
            self.log.log('[-] Error is '+str(e))


    def __input_sans(self,driver,sans):
        try:
            driver.find_element_by_id(repo['sans']).click()
            driver.find_element_by_id(repo['sans']).send_keys(sans)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @__input_sans')
            self.log.log('[-] Error is '+str(e))

    def __input_emails(self,driver,emails):
        try:
            driver.find_element_by_id(repo['emails']).clear()
            driver.find_element_by_id(repo['emails']).send_keys(emails)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @__input_emails')
            self.log.log('[-] Error is '+str(e))

    def __input_common_name(self,driver,common_name):
        try:
            driver.find_element_by_id(repo['common_name']).clear()
            driver.find_element_by_id(repo['common_name']).send_keys(common_name)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @__input_common_name')
            self.log.log('[-] Error is '+str(e))

    def __input_comments(self,driver,comments):
        try:
            driver.find_element_by_id(repo['comment']).click()
            driver.find_element_by_id(repo['comment']).send_keys(comments)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @__input_comments')
            self.log.log('[-] Error is '+str(e))

    def __select_from_options_by_name(self,option_value,select_box):
        try:
            option_value = option_value.strip().lower()
            options = [item for item in select_box.find_elements_by_tag_name('option')]
            for element in options:
                element_value = element.get_attribute("value").strip().lower()
                element_text = element.text
                if element_value == option_value or element_text == option_value:
                    element.click()
        except Exception as er:
            self.log.log("Error occur @__select_from_options_by_name")
            self.log.log("Error is " +str(er))

    def __select_from_options_by_index(self,index,select_box):
        try:
            options = [item for item in select_box.find_elements_by_tag_name('option')]
            idx = int(index) % len(options)
            options[idx].click()
            time.sleep(2)
        except Exception as er:
            self.log.log("Error occur @__select_from_options_by_index")
            self.log.log("Error is " +str(er))

    def __select_from_radio_by_name(self,selected,radio_button):
        try:
            option_value = str(selected).strip().lower()
            options = [item for item in radio_button.find_elements_by_name(repo['validity'])]
            for element in options:
                element_value = element.get_attribute("value").strip().lower()
                element_text = element.text
                if element_value == option_value or element_text == option_value:
                    element.click()
        except Exception as er:
            self.log.log("Error occur @__select_from_radio_by_name")
            self.log.log("Error is " +str(er))

    def __upload_csr(self,driver,filePath):
        try:
            driver.find_element_by_id(repo['upload']).send_keys(filePath)
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @__upload_csr')
            self.log.log('[-] Error is '+str(e))

    def click_upload_button(self,driver):
        try:
            # elem = driver.find_element_by_class_name(repo['upload_safari'])
            a = repo['upload_safari']
            self.log.log("TEST COMES HERE!!")
            elem = driver.find_element_by_class_name(repo['upload_safari'])
            elem.click()
            # elem.click()
            # click_script = "if ( document.createEvent ) {" \
            #                "var evt = document.createEvent('MouseEvents');" \
            #                "evt.initEvent('click', true, false);" \
            #                "arguments[0].dispatchEvent(evt);" \
            #                "} else if( document.createEventObject ) {" \
            #                "arguments[0].fireEvent('onclick') ;	" \
            #                "} else if (typeof arguments[0].onclick == 'function' ) {" \
            #                "arguments[0].onclick();	" \
            #                "arguments[0].onclick.apply(arguments[0]);" \
            #                "}"
            # driver.execute_script(click_script,elem)
        except Exception as e:
            self.log.log('[-] Error occur @click_upload_button')
            self.log.log('[-] Error is '+str(e))

    def __upload_csr_safari(self,driver,filePath):
        try:
            self.click_upload_button(driver)
            applescriptCommand ="tell application \"System Events\"\n" \
                                 "delay 2 \n" \
                                 "keystroke \"G\" using {command down, shift down}\n " \
                                 "delay 2 \n" \
                                 "keystroke \""+filePath+"\"\n" \
                                 "delay 2 \n" \
                                 "keystroke return \n" \
                                 "delay 2 \n" \
                                 "keystroke return \n" \
                                 "end tell"
            subprocess.Popen(['osascript','-e',applescriptCommand])
            time.sleep(8)
        except Exception as e:
            self.log.log('[-] Error occur @__upload_csr_safari')
            self.log.log('[-] Error is '+str(e))

    def get_common_name(self):
        try:
            driver = self.driver
            cn = driver.find_element_by_id(repo['common_name']).text
            return cn
        except Exception as e:
            self.log.log('[-] Error occur @get_common_name')
            self.log.log('[-] Error is '+str(e))

    def get_org_name(self):
        try:
            driver = self.driver
            on = driver.find_element_by_id(repo['org_name']).text
            return on
        except Exception as e:
            self.log.log('[-] Error occur @get_org_name')
            self.log.log('[-] Error is '+str(e))

    def get_org_unit(self):
        try:
            driver = self.driver
            on = driver.find_element_by_id(repo['org_unit']).text
            return on
        except Exception as e:
            self.log.log('[-] Error occur @get_org_unit')
            self.log.log('[-] Error is '+str(e))

    def submit_form(self):
        driver = self.driver
        try:
            driver.by_id(repo['submit']).click()
        except Exception as er:
            self.log.log("Error occur @_select_from_options_by_index")
            self.log.log("Error is " +str(er))

    def input_data_SSLPC(self,ca_name,email_group,csr,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_SSLMDC(self,ca_name,email_group,csr,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)


    def input_data_SSLWC(self,ca_name,email_group,csr,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_SSLEVPC(self,ca_name,email_group,csr,server_platform_index,period,comments='test'):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_SSLEVMDC(self,ca_name,email_group,csr,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_SSLCC(self,ca_name,email_group,csr,server_platform_index,period,comments='test',sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_CPC(self,ca_name,email_group,csr,common_name,emails,period,auto_renew_index):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        auto_select_box = driver.by_id(repo['auto_renew'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__input_common_name(driver,common_name)
        self.__input_emails(driver,emails)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(auto_renew_index,auto_select_box)

    def input_data_CEPCC(self,ca_name,email_group,common_name,emails,period,auto_renew_index):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        auto_select_box = driver.by_id(repo['auto_renew'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_emails(driver,emails)
        self.__input_common_name(driver,common_name)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(auto_renew_index,auto_select_box)


    def input_data_CDSPC(self,ca_name,email_group,csr,common_name,emails,period,auto_renew_index):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        auto_select_box = driver.by_id(repo['auto_renew'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__input_common_name(driver,common_name)
        self.__input_emails(driver,emails)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(auto_renew_index,auto_select_box)

    def input_data_CSC(self,ca_name,email_group,csr,server_platform_index,period,comment):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_csr(driver,csr)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comment)

    def input_data_EVCSC(self):
        pass

    def input_data_by_upload_SSLMDC(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__input_comments(driver,comments)
        self.__upload_csr(driver,csr_file_path)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)


    def input_data_by_upload_SSLPC(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)



    def input_data_by_upload_SSLWC(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_SSLEVPC(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_SSLEVMDC(self,ca_name,email_group,csr,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_SSLCC(self,ca_name,email_group,csr,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_CPC(self,ca_name,email_group,csr,common_name,emails,period,auto_renew_index):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        auto_select_box = driver.by_id(repo['auto_renew'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr)
        self.__input_common_name(driver,common_name)
        self.__input_emails(driver,emails)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(auto_renew_index,auto_select_box)



    def input_data_by_upload_CDSPC(self,ca_name,email_group,csr,common_name,emails,period,auto_renew_index):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        auto_select_box = driver.by_id(repo['auto_renew'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr)
        self.__input_common_name(driver,common_name)
        self.__input_emails(driver,emails)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(auto_renew_index,auto_select_box)

    def input_data_by_upload_CSC(self,ca_name,email_group,csr_file_path,server_platform_index,period,comment):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comment)

    def input_data_by_upload_SSLMDC_safari(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.click_upload_button(driver)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)


    def input_data_by_upload_SSLPC_safari(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)



    def input_data_by_upload_SSLWC_safari(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_SSLEVPC_safari(self,ca_name,email_group,csr_file_path,server_platform_index,period,comments):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_SSLEVMDC_safari(self,ca_name,email_group,csr,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_SSLCC_safari(self,ca_name,email_group,csr,server_platform_index,period,comments,sans=''):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr)
        self.__input_sans(driver,sans)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comments)

    def input_data_by_upload_CPC_safari(self,ca_name,email_group,csr,common_name,emails,period,auto_renew_index):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        auto_select_box = driver.by_id(repo['auto_renew'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr)
        self.__input_common_name(driver,common_name)
        self.__input_emails(driver,emails)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(auto_renew_index,auto_select_box)


    def input_data_by_upload_CDSPC_safari(self,ca_name,email_group,csr,common_name,emails,period,auto_renew_index):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        auto_select_box = driver.by_id(repo['auto_renew'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr)
        self.__input_common_name(driver,common_name)
        self.__input_emails(driver,emails)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(auto_renew_index,auto_select_box)

    def input_data_by_upload_CSC_safari(self,ca_name,email_group,csr_file_path,server_platform_index,period,comment):
        driver = self.driver
        ca_select_box = driver.by_id(repo['ca'])
        mail_group_select_box = driver.by_id(repo['email_group'])
        server_type_select_box = driver.by_id(repo['server_type'])
        period_radio = driver.by_id(repo['radio_validity'])
        self.__select_from_options_by_name(ca_name,ca_select_box)
        self.__select_from_options_by_name(email_group,mail_group_select_box)
        self.__upload_csr_safari(driver,csr_file_path)
        self.__select_from_radio_by_name(period,period_radio)
        self.__select_from_options_by_index(server_platform_index,server_type_select_box)
        self.__input_comments(driver,comment)

    def type_csr_generation_link(self):
        driver = self.driver
        driver.by_id(repo['csr']).click()
        time.sleep(1)
        driver.find_element_by_link_text(repo['csr_generate_link']).click()
        time.sleep(3)


    def get_title(self):
        return super(RequestCertPage,self).get_title()