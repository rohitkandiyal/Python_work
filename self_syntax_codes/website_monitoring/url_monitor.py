from http.client import HTTPConnection
import logging, sys


url_list=["python.org","http://python.org","www.python.org"]
logging.basicConfig(filename='abc.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S')

def fetch_response_status(url):
    try
        connection = HTTPConnection(url)
        connection.request("GET", "/")
        response = connection.getresponse()
        return response.status
    except HTTPException as error:
        logging.error('HTTP connection threw error:', error)
    except Exception as e:
        logging.info('Undefined URL:', url)
        logging.error('Error is:', e)

def website_check(url):
    resp = fetch_response_status(url)
    if (resp == 200):
        return "Success"
    else:
        return "Failure"
        logging.error("Website unreachable..")

def internet_available():
    try:
        r=website_check("www.google.com")
    except Exception:
        logging.error("Website response failed..") 
    
    if (r == "Success"):
        logging.info("Internet Connection Established")
        return True
    else:
        logging.error("Internet Unavailable")


for url in url_list:

