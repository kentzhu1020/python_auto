# coding=utf-
from selenium.webdriver import ActionChains
import sys
from selenium.webdriver.common.keys import Keys
from Model.Log import logger
import commands
import os
import subprocess
import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui

__author__ = 'kzhu'

class Base(object):

    def __init__(self,browser):
        self.driver = self.set_up(browser)
        self.element_selector_setting()
        self.wait = ui.WebDriverWait(self.driver, 5)

    def set_up(self,browser_name):
        log = logger()
        cmd = "netstat -an | grep '4444'|awk '{print $6}'"
        dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        browser_name = browser_name.decode('utf-8').lower()
        try:
            if browser_name == 'chrome':
                browser = webdriver.Chrome()
            elif browser_name == 'safari':
                subprocess.Popen(["java", "-jar",dir_path+"/Selenium/selenium-server-standalone-2.48.2.jar"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
                output = commands.getoutput(cmd)
                while 1:
                    if output == '':
                        time.sleep(1)
                        output = commands.getoutput(cmd)
                    else :
                        break
                browser = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.SAFARI)
            else:
                browser = webdriver.Firefox()
            return browser
        except Exception as er:
            pid = commands.getoutput("ps -eaf|grep -i 'selenium'|grep -v grep|awk '{print $2}'")
            if len(pid) != 0:
                log.log("[+] Force killing the process with signal at the beginning of testing")
                os.system("kill -9 "+ pid)
            log.log("[-] Error occur @set_up")
            log.log("[-] The Error is set up browser driver failed, details is "+str(er))
            sys.exit()

    def element_selector_setting(self):
        self.driver.by_id = self.driver.find_element_by_id
        self.driver.by_xpath = self.driver.find_element_by_xpath
        self.driver.by_name = self.driver.find_element_by_name
        self.driver.by_tag_name = self.driver.find_element_by_tag_name
        self.driver.by_css_selector = self.driver.find_element_by_css_selector
        self.driver.by_link_text = self.driver.find_element_by_link_text
        self.driver.by_partial_link_text = self.driver.find_element_by_partial_link_text
        self.driver.by_class_name = self.driver.find_element_by_class_name

    def drag_and_drop(self, driver,elem, target):
        ActionChains(driver).drag_and_drop(elem, target).perform()

    def move_to_element(self,driver,elem):
        ActionChains(driver).move_to_element(elem).perform()

    def get_current_url(self):
        this_url = self.driver.current_url
        return this_url

    def get_title(self):
        this_title = self.driver.title
        return this_title

    def clear_cookies(self):
        self.driver.delete_all_cookies()


    def scroll_to_element(self,driver,css_selector):
        height = driver.execute_script("return document.querySelector(\'"+css_selector+"\').getBoundingClientRect().top")
        driver.execute_script("window.scrollBy(0, "+str(height)+");")

    def scroll_to_bottom(self,driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self,driver):
        driver.execute_script("window.scrollTo(0, 0);")

    def take_screenshot(self,name,save_location):
        # Make sure the path exists.
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = '%s/%s' % (path, name)
        self.driver.get_screenshot_as_file(full_path)
        return full_path

    def right_click_on_menu(self,driver,elem,index):
        if index ==1:
            pass
        else:
            pass
        ActionChains(driver).context_click(elem).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()

    def drag_and_drop_by_js(self,driver,css_selector,target):
        position_x = driver.execute_script("return document.querySelector(\'"+css_selector+"\').getBoundingClientRect().right")
        position_y = driver.execute_script("return document.querySelector(\'"+css_selector+"\').getBoundingClientRect().top")
        dragdrop_string = "function simulate(f,c,d,e){var b,a=null;for(b in eventMatchers)if(eventMatchers[b].test(c)){a=b;break}if(!a)return!1;document.createEvent?(b=document.createEvent(a),a==\"HTMLEvents\"?b.initEvent(c,!0,!0):b.initMouseEvent(c,!0,!0,document.defaultView,0,d,e,d,e,!1,!1,!1,!1,0,null),f.dispatchEvent(b)):(a=document.createEventObject(),a.detail=0,a.screenX=d,a.screenY=e,a.clientX=d,a.clientY=e,a.ctrlKey=!1,a.altKey=!1,a.shiftKey=!1,a.metaKey=!1,a.button=1,f.fireEvent(\"on\"+c,a));return!0} var eventMatchers={HTMLEvents:/^(?:load|unload|abort|error|select|change|submit|reset|focus|blur|resize|scroll)$/,MouseEvents:/^(?:click|dblclick|mouse(?:down|up|over|move|out))$/};simulate(arguments[0],\"mousedown\",0,0); simulate(arguments[0],\"mousemove\",arguments[1],arguments[2]); simulate(arguments[0],\"mouseup\",arguments[1],arguments[2]);"
        driver.execute_script(dragdrop_string,target,position_x,position_y)

    def move_to_element_by_js(self,driver,target):
        mouseOverScript = "if(document.createEvent){var evObj = document.createEvent('MouseEvents');evObj.initEvent('mouseover', true, false); arguments[0].dispatchEvent(evObj);} else if(document.createEventObject) { arguments[0].fireEvent('onmouseover');}"
        driver.execute_script(mouseOverScript,target)

    def quit(self,browser=''):
        self.driver.quit()
        if browser.decode('utf-8').lower() == 'safari':
            self.kill_selenium_process()

    def kill_selenium_process(self):
        pid = commands.getoutput("ps -eaf|grep -i 'selenium'|grep -v grep|awk '{print $2}'")
        log = logger()
        try:
            log.log("[+] Kill the running selenium process")
            os.system('kill -9 '+pid)
        except Exception as er:
            if len(pid) !=0:
                log.log("[-] Failed to kill the process but force it to")
                log.log("[-] Error is "+str(er))
                os.system('kill -9 '+pid)



# if __name__ == '__main__':
#     base  = Base('safari')

