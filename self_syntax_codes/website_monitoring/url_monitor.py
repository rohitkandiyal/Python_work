#!/usr/bin/python

import requests
from smtplib import SMTP
import logging, sys

#https://na1.dev.nice-incontact.com/    https://na12.dev.nice-incontact.com/
url_list=["python.org","http://python.org","www.python.org","https://na1.dev.nice-incontact.com/","na1.dev.nice-incontact.com/","www.na12.dev.nice-incontact.com/"]
logging.basicConfig(filename='site_access.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S')

#
def check_http_url(url_to_validate):
    try:
        response = requests.get(url_to_validate)
        return response.status_code
    except requests.ConnectionError as exception:
        logging.error("URL: {} does not exist on Internet".format(url_to_validate))

#Setting URLs to http for requests module:Better error handling and redirects
def set_http_url(url):
    if (url.startswith("http://") or url.startswith("https://")):
        return url
    elif (url.startswith("www.")):
        return url.replace("www.","http://",1)
    else:
        return "{}{}".format("http://",url)

#Separate function to abstract the http client module
def website_check(url):
    url=set_http_url(url)
    return check_http_url(url)

def internet_available():
    try:
        r=website_check("http://google.com")
        r1=website_check("http://facebook.com")
    except:
        logging.error("Website response failed..") 
    
    if (r == 200) or (r1 == 200):
        logging.info("Internet Connection Established")
        return True
    else:
        return False

def send_email(receiver,subject):
    port = 587
    smtp_server = "smtp.gmail.com"
    e_sender = "kandiyalrohitabcd@gmail.com"
    e_receiver = receiver
    password = "Symantec@123"
    email_content = "Subject: {}".format(subject)
    with SMTP(smtp_server, port) as server:
        try:
            server.starttls()
            server.login("kandiyalrohitabcd", password)
            server.sendmail(e_sender, e_receiver, email_content)
            logging.info('Error email sent to {}'.format(e_receiver))
        except SMTPException:
            logging.error('SMTPException error')
        except:
            logging.error('SMTP connection Error')


logging.info("++++++++++++++++++++++Starting URL {} health check++++++++++++++++++++++".format(url_list))
if internet_available():
    for url in url_list:
        logging.info("Checking URL {} ".format(url))
        resp = website_check(url)
        if (resp == 200):
            logging.info("{0} is ACTIVE.".format(url))
        else:
            logging.error("{0} is INACTIVE. STATUS CODE: {1}".format(url,resp))
            subject_content="{} : URL check has failed with status code: {}".format(url,resp)
            receiver_list=["kandiyalrohit@gmail.com"]
            for receiver in receiver_list:
                send_email(receiver,subject_content)
else:
    logging.error("Internet Unavailable")

    
