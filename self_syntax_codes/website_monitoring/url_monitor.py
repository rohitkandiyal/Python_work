#!/usr/bin/python

from http.client import HTTPConnection, HTTPException, socket
from smtplib import SMTP
import requests
import logging, sys

#https://na1.dev.nice-incontact.com/    https://na12.dev.nice-incontact.com/
url_list=["python.org","http://python.org","www.python.org","https://na1.dev.nice-incontact.com/","na1.dev.nice-incontact.com/","www.na12.dev.nice-incontact.com/"]
logging.basicConfig(filename='site_access.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S')

def fetch_response_status(url):
    try:
        connection = HTTPConnection(url)
        connection.request("GET", "/")
        response = connection.getresponse()
        return response.status
    except HTTPException:
        logging.error('HTTPException error')
    except socket.error:
        logging.error('Socket error')
    except:
        logging.error('Invalid URL:', url)
        logging.error('HTTP connection Error')

def check_http_url(url_to_validate):
    try:
        response = requests.get(url_to_validate)
        logging.info("URL: {} is valid and exists on the internet".format(url_to_validate))
        return response.status_code
    except requests.ConnectionError as exception:
        logging.error("URL: {} does not exist on Internet".format(url_to_validate))

def set_http_url(url):
    if (url.startswith("http://") or url.startswith("https://")):
        return url
    elif (url.startswith("www.")):
        return url.replace("www.","http://",1)
    else:
        return "{}{}".format("http://",url)

def website_check(url):
    url=set_http_url(url)
    resp = check_http_url(url)
    '''
    if (url.startswith("http")):
        resp = check_http_url(url)
    else:
        resp = fetch_response_status(url)
    '''
    if (resp == 200):
        return "Success"
    else:
        return "Failure"
        logging.error("URL unreachable:", url)

def internet_available():
    try:
        r=website_check("http://google.com")
        r1=website_check("http://facebook.com")
    except:
        logging.error("Website response failed..") 
    
    if (r == "Success") or (r1 == "Success"):
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
        except SMTPException:
            logging.error('SMTPException error')
        except:
            logging.error('SMTP connection Error')


logging.info("++++++++++++++++++++++Starting URL {} health check++++++++++++++++++++++".format(url_list))
if internet_available():
    for url in url_list:
        url = set_http_url(url)
        logging.info("Checking URL {} ".format(url))
        if (website_check(url) == "Success"):
            logging.info("{0} is ACTIVE.".format(url))
        else:
            logging.error("{0} is INACTIVE.".format(url))
            '''subject_content="{} : URL IS UNRESPONSIVE".format(url)
            receiver_list=["kandiyalrohit@gmail.com"]
            for receiver in receiver_list:
                send_email(receiver,body)'''
else:
    logging.error("Internet Unavailable")

    
