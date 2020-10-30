from http.client import HTTPConnection, HTTPException, socket
import logging, sys


url_list=["python.org","http://python.org","www.python.org"]
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
        logging.info('Undefined URL:', url)
        logging.error('HTTP connection Error')

def website_check(url):
    resp = fetch_response_status(url)
    if (resp == 200):
        return "Success"
    else:
        return "Failure"
        logging.error("Website unreachable:", url)

def internet_available():
    try:
        r=website_check("www.google.com")
    except:
        logging.error("Website response failed..") 
    
    if (r == "Success"):
        logging.info("Internet Connection Established")
        return True
    else:
        logging.error("Internet Unavailable")
        return False


logging.info("+++++++++++++++++++++++++++++++++Starting URL health check+++++++++++++++++++++++++++++++++++++++++")
if internet_available():
    print("PASS")
else:
    print("FAIL")
#for url in url_list:
    

