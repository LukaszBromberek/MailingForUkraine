from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from random import randrange
import smtplib
import getpass
import argparse

from messages.test import TEST_MESSAGE
from messages.images2702 import REFUGEES_2702, YOUR_SOLDIERS_2702

MESSAGES = {
    #TEST_MESSAGE.short_name : TEST_MESSAGE.message
    REFUGEES_2702.short_name : REFUGEES_2702, YOUR_SOLDIERS_2702.short_name: YOUR_SOLDIERS_2702
    }

if __name__ == "__main__":

    ## To send specific message
    ## ---------------------------
        
    # parser = argparse.ArgumentParser(description='Select message')
    # parser.add_argument('message', type=str, required=False,
    #                     help='Name of the message to send.')

    
    # args = parser.parse_args()
    # message = MESSAGES[args.message]
 
 
    ## To send random message
    ## ---------------------------
    ms_count = len(list(MESSAGES.keys()))
    message = MESSAGES[list(MESSAGES.keys())[randrange(0, ms_count-1)]]

    with open("mails.txt", "r") as file:
        send_to = file.readlines()
    
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    #smtp.login(input("Your gmail address : "), getpass.getpass("Your email password : "))
    smtp.login("yours@gmail.com", "your password")
    for address in send_to:
        smtp.sendmail(from_addr="Ukrainian news",
                    to_addrs=address, msg=message.message.as_string())
    
    smtp.quit()