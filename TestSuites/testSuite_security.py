import csv
import os
import subprocess
import  unittest
from Model.Result import TestResult
from Model.Utility import Utilities


__author__ = 'kzhu'

class SecurityCheck(unittest.TestCase):

    command = 'nmap --script ssl-enum-ciphers -p 443'.split()

    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]
        self.util = Utilities()

    def _read_command_output(self,command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = p.communicate()
        return out

    def _get_index(self,str,list):
        index = 0
        for index in range(0,len(list)):
            if str in list[index]:
                break
        if (index == len(list)-1): #No such str in the list
            index = -1
        return index

    def _read_command_output_line_by_line(self,command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')

    def test_checkSSLv3(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(BASE_DIR+'/Data/domains_data.csv') as configfile:
            reader = csv.DictReader(configfile)
            for row in reader:
                dns = row['domain']
                self.command.append(dns)
                try:
                    output = self.util.read_command_output(self.command)
                    output = output.split('\n')
                    index = self.util.get_index('SSLv3',output)
                    if index != -1:
                        self.assertNotIn('TLS_',output[index+2],'Domain '+dns+' support SSlv3 ! Please disable it!')
                        TestResult().addSuccess(self.suite_name,0,self.case_name+'_'+row['#'],'')
                    else:
                        self.assertTrue(True)
                        TestResult().addSuccess(self.suite_name,0,self.case_name+'_'+row['#'],'')
                except AssertionError as ae:
                    TestResult().addFail(self.suite_name,1,self.case_name+'_'+row['#'],str(ae))
                except Exception as e:
                    TestResult().addError(self.suite_name,2,self.case_name+'_'+row['#'],str(e))
                self.command.remove(dns)

    def test_checkRC4Cipher(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(BASE_DIR+'/Data/domains_data.csv') as configfile:
            reader = csv.DictReader(configfile)
            for row in reader:
                dns = row['domain']
                self.command.append(dns)
                try:
                    for line in self.util.read_command_output_line_by_line(self.command):
                        if '_RC4' in line:
                            self.assertTrue(False,'Domain '+dns+' support RC4 !Please disable it!')
                    TestResult().addSuccess(self.suite_name,0,self.case_name+'_'+row['#'],'')
                except AssertionError as ae:
                    TestResult().addFail(self.suite_name,1,self.case_name+'_'+row['#'],str(ae))
                except Exception as e:
                    TestResult().addError(self.suite_name,2,self.case_name+'_'+row['#'],str(e))
                self.command.remove(dns)

    def test_checkCSRF(self):
        pass

    def tearDown(self):
        del self.util


if __name__ == "__main__":
    unittest.main()