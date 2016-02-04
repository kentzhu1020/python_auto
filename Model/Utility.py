import base64
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
from os.path import basename
import smtplib
import subprocess
import psycopg2
from pylab import *
import time

__author__ = 'kzhu'
class EMAIL_TMPL(object):
    # Create the body of the message (a plain-text and an HTML version).
    TEXT_TMPL = "Hi!\nThis is an automatic reminder, Please do not reply directly.\n" \
        # + "\n\tname: %s"\
        # + "\n\torder id: %s "\
        # + "\n\tserial number: %s" \
        # + "\n\n\nThanks,\nBbCerts",


class Utilities(EMAIL_TMPL):

    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        today = time.strftime("%Y%m%d")
        self.chart_dir = self.path+'/Results'
        self.chart_file = self.chart_dir+'/report_'+today+'.png'


    def _get_keys(self,dictionary,value):
        keys = []
        for key in dictionary:
            if dictionary[key] == value:
                keys.append(key)
        return keys

    def draw_report_pie_chart(self,fracs):
        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8,0.8])
        colors = {'Passed':'lightgreen','Failed':'orangered','Error':'orange'}
        explode = {'Passed':0,'Failed':0,'Error':0}
        keys = self._get_keys(fracs,0)
        labels_fracs = {k: v for k, v in fracs.items() if k not in keys}
        labels_color = {k: v for k, v in colors.items() if k not in keys}
        labels_explode = {k: v for k, v in explode.items() if k not in keys}
        final_explode = labels_explode.values()
        final_colors = labels_color.values()
        final_fracs = labels_fracs.values()
        labels = labels_fracs.keys()
        pie(final_fracs, explode=final_explode, labels=labels,
                        autopct='%1.1f%%', shadow=False, startangle=90, colors=final_colors)
        title('Testing Report Summary')
        if os.path.isdir(self.chart_dir):
            savefig(self.chart_file)
        else:
            os.system("mkdir -p "+self.chart_dir)
            savefig(self.chart_file)
        return self.chart_file


    def send_mail(self,email_from,email_to,fileToSend):
        today = time.strftime("%Y%m%d")
        msg = MIMEMultipart()
        msg["From"] = email_from
        msg["To"] = email_to
        msg['Subject'] = "Automation Testing Report On "+ today
        msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=basename(fileToSend))
        msg.attach(attachment)

        part1 = MIMEText(self.TEXT_TMPL, 'plain')
        msg.attach(part1)
        server = smtplib.SMTP("10.75.106.10:25")
        # server.starttls()
        # server.login(username,password)
        server.sendmail(email_from, email_to, msg.as_string())
        server.close()


    def read_command_output(self,command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = p.communicate()
        return out

    def get_index(self,str,list):
        index = 0
        for index in range(0,len(list)):
            if str in list[index]:
                break
        if (index == len(list)-1): #No such str in the list
            index = -1
        return index

    def read_command_output_line_by_line(self,command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')

class DBConnection(object):

    db_pw = "cm9vdA=="
    password = base64.b64decode(db_pw)

    db_config = {
        'user': 'root',
        'password': password,
        'host': 'localhost',
        'database': 'certificatedb',
        'port': '5432',
    }
    def get_user_email_address(self,user_name):
        conn = psycopg2.connect(**self.db_config)
        cursor = conn.cursor()
        query = "SELECT email FROM auth_user WHERE username = '" +str(user_name)+ "';"
        # cursor.execute("SELECT email FROM auth_user WHERE username = '%s';" %user_name)  Not safe!
        cursor.execute(query)
        email = cursor.fetchone()
        cursor.close()
        conn.close()
        return email[0].lower()

if __name__ == "__main__":
    db = DBConnection()
    print db.get_user_email_address('kzhu')
