from http.client import HTTPConnection


url_list=["python.org","http://python.org","www.python.org"]

def fetch_response_status(url):
    connection = HTTPConnection(url)
    connection.request("GET", "/")
    response = connection.getresponse()
    return response.status,response.reason


logging.basicConfig(filename='abc.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S')


for url in url_list:
    
