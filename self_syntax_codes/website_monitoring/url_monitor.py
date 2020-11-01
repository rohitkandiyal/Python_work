#!/usr/bin/python

import requests,re
from email.message import EmailMessage
from smtplib import SMTP
import logging, sys

#url_list=["python.org","http://python.org","www.python.org","https://na1.dev.nice-incontact.com/","http://www.google.com/wework","www.na12.dev.nice-incontact.com/"]
url_list=sys.argv[1].split(",")
receiver_list=sys.argv[2].split(",")
LOG_FILE='site_access.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S')
body="Server sent no HTTP error response"

#
def check_http_url(url_to_validate):
    global body
    try:
        response = requests.get(url_to_validate)
        return response.status_code
        response.raise_for_status()
    except requests.HTTPError as httperr:
        logging.error("URL: {} throws Http Error: {}".format(url_to_validate,httperr))
        body = str(httperr)
    except requests.ConnectionError as connerr:
        logging.error("URL: {} throws connection error: {}".format(url_to_validate,connerr))
        body = str(connerr)
    except requests.RequestException as err:
        logging.error("URL: {} connection failed".format(url_to_validate))
        body = str(err)

#Setting URLs to http for requests module:Better error handling and redirects
def set_http_url(url):
    if (url.startswith("http://") or url.startswith("https://")):
        return url
    elif (url.startswith("www.")):
        return url.replace("www.","http://",1)
    else:
        return "{}{}".format("http://",url)

#additional check to validate the URL formation
def validate_url(url):
    if(" " in url):
        return False
    else:
        pass
#check the validate the email id
def validate_email(email_id):
    regex_obj=re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    if(re.search(regex_obj,email_id)):
        return True
    else:
        return False

                   
#Separate function to abstract the http client module
def website_check(url):
    url=set_http_url(url)
    return check_http_url(url)

def internet_available():
    logging.info("Checking internet connection..")
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

def send_email(e_receiver,subject):
    port = 587
    smtp_server = "smtp.gmail.com"
    global body
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "kandiyalrohitabcd@gmail.com"
    msg['To'] = e_receiver
    password = "Symantec@123"
    if (validate_email(e_receiver)):
        with SMTP(smtp_server, port) as server:
            try:
                server.starttls()
                server.login("kandiyalrohitabcd", password)
                server.send_message(msg)
                logging.info('Error email sent to {}'.format(e_receiver))
            except SMTPException:
                logging.error('SMTPException error')
            except:
                logging.error('SMTP connection Error')
    else:
        logging.error("Email ID {} is Invalid".format(e_receiver))


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
            #receiver_list=["kandiyalrohit@gmail.com"]
            for receiver in receiver_list:
                send_email(receiver,subject_content)
else:
    logging.error("Internet Unavailable")
    sys.exit(1)

    
