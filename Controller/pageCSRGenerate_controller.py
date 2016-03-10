import time
from Controller.base import Base
from Model.Log import logger
from Views.csr_generate_view import repo

__author__ = 'kzhu'

class CSRPage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)
        self.logger = logger()


    def __input_common_name(self,driver,cn):
        try:
            driver.find_element_by_id(repo['common_name']).click()
            driver.find_element_by_id(repo['common_name']).clear()
            driver.find_element_by_id(repo['common_name']).send_keys(cn)
            time.sleep(2)
        except Exception as e:
            self.logger.log('[-] Error occur @__input_common_name')
            self.logger.log('[-] Error is '+str(e))

    def __input_sans(self,driver,san):
        try:
            driver.find_element_by_id(repo['sans']).clear()
            driver.find_element_by_id(repo['sans']).send_keys(san)
            time.sleep(2)
        except Exception as e:
            self.logger.log('[-] Error occur @__input_sans')
            self.logger.log('[-] Error is '+str(e))

    def __input_organization(self,driver,org):
        try:
            driver.find_element_by_id(repo['organization']).clear()
            driver.find_element_by_id(repo['organization']).send_keys(org)
            time.sleep(2)
        except Exception as e:
            self.logger.log('[-] Error occur @__input_organization')
            self.logger.log('[-] Error is '+str(e))

    def __input_city(self,driver,city):
        try:
            driver.find_element_by_id(repo['city']).clear()
            driver.find_element_by_id(repo['city']).send_keys(city)
            time.sleep(2)
        except Exception as e:
            self.logger.log('[-] Error occur @__input_city')
            self.logger.log('[-] Error is '+str(e))

    def __input_state(self,driver,state):
        try:
            driver.find_element_by_id(repo['state']).clear()
            driver.find_element_by_id(repo['state']).send_keys(state)
            time.sleep(2)
        except Exception as e:
            self.logger.log('[-] Error occur @_input_state')
            self.logger.log('[-] Error is '+str(e))

    def __input_department(self,driver,depart):
        try:
            driver.find_element_by_id(repo['department']).clear()
            driver.find_element_by_id(repo['department']).send_keys(depart)
            time.sleep(2)
        except Exception as e:
            self.logger.log('[-] Error occur @__input_department')
            self.logger.log('[-] Error is '+str(e))


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
            self.logger.log("Error occur @__select_from_options_by_name")
            self.logger.log("Error is " +str(er))

    def __select_from_options_by_index(self,index,select_box):
        try:
            options = [item for item in select_box.find_elements_by_tag_name('option')]
            idx = int(index) % len(options)
            options[idx].click()
            time.sleep(2)
        except Exception as er:
            self.logger.log("Error occur @__select_from_options_by_index")
            self.logger.log("Error is " +str(er))

    def input_data_csr(self,common_name,org,city,state,department,country_index,key_size_index,sans=''):
        try:
            driver = self.driver
            country_select_box = driver.by_id(repo['country'])
            key_size_select_box = driver.by_id(repo['key_size'])
            self.__input_common_name(driver,common_name)
            self.__input_sans(driver,sans)
            self.__input_organization(driver,org)
            self.__input_city(driver,city)
            self.__input_state(driver,state)
            self.__input_department(driver,department)
            self.__select_from_options_by_index(country_index,country_select_box)
            self.__select_from_options_by_index(key_size_index,key_size_select_box)
        except Exception as er:
            self.logger.log("Error occur @input_data_csr")
            self.logger.log("Error is " +str(er))

    def click_generate(self):
        driver =self.driver
        driver.find_element_by_xpath(repo['generate_button']).click()
        time.sleep(2)

    def return_to_request_cert(self):
        try:
            driver =self.driver
            driver.find_element_by_partial_link_text(repo['request_cert']).click()
            time.sleep(2)
        except Exception as er:
            self.logger.log("Error occur @return_to_request_cert")
            self.logger.log("Error is " +str(er))


    def get_title(self):
        return super(CSRPage,self).get_title()

