import time
from Controller.base import Base
from Model.Log import logger
from Views.home_view import repo

__author__ = 'kzhu'

class HomePage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)

    def navigate_to_sub_menu(self,sub_menu_name):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_request_cert']).click()
            sub_menu_lists = driver.find_elements_by_xpath(repo['certificate_requests'])
            for sub_menu_item in sub_menu_lists:
                sub_menu_innerHTML = sub_menu_item.text.encode('utf-8').lower()
                if sub_menu_innerHTML == sub_menu_name.lower():
                    sub_menu_item.click()
                    time.sleep(2)
                    break
        except Exception as er:
            log.log('[-] Error occur @navigate_to_sub_menu')
            log.log('[-] Error is '+str(er))

    # def navigate_to_sub_menu(self,sub_menu_name):
    #     log = logger()
    #     driver = self.driver
    #     try:
    #         driver.by_link_text(repo['navigation_request_cert']).click()
    #         driver.by_link_text(sub_menu_name).click()
    #     except Exception as er:
    #         log.log('[-] Error occur @navigate_to_sub_menu')
    #         log.log('[-] Error is '+str(er))
    def navigate_to_sub_links(self,link_text):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_request_cert']).click()
            driver.by_partial_link_text(link_text).click()
            time.sleep(2)
        except Exception as er:
            log.log('[-] Error occur @navigate_to_sub_menu')
            log.log('[-] Error is '+str(er))


    def navigate_to_home(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_home']).click()
            time.sleep(2)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_home')
            log.log('[-] Error is '+str(e))

    def navigate_to_view_cert(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_view_certs']).click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_view_cert')
            log.log('[-] Error is '+str(e))

    def navigate_to_notification_group(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_notification_group']).click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_notification_group')
            log.log('[-] Error is '+str(e))

    def navigate_to_help(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_help']).click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_help')
            log.log('[-] Error is '+str(e))

    def logout(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['logout']).click()
            time.sleep(2)
        except Exception as e:
            log.log('[-] Error occur @logout')
            log.log('[-] Error is '+str(e))

    def get_user_email_address(self):
        log = logger()
        driver = self.driver
        try:
            email_address = driver.by_class_name(repo['login_email_address']).text
            return str(email_address).lower()
        except Exception as e:
            log.log('[-] Error occur @get_user_email_address')
            log.log('[-] Error is '+str(e))

    def get_title(self):
        return super(HomePage,self).get_title()

