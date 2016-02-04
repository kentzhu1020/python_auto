__author__ = 'kzhu'
import datetime
import time
import os

class logger:

    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        today = time.strftime("%Y%m%d")
        self.log_dir = self.path+'/Log'
        self.log_file = self.log_dir+'/logger_'+today+'.log'
        try:
            self.log_fp = open(self.log_file,'a')
        except:
            pass

    def log(self,message=''):
        if os.path.isfile(self.log_file):
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            self.log_fp.write("%s\t%s\n" % (now, message))
        else:
            os.system("mkdir -p "+self.log_dir)
            os.system("touch "+self.log_file)
            self.log_fp = open(self.log_file, 'a')
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            self.log_fp.write("%s\t%s\n" % (now, message))
            self.log_fp.close()
