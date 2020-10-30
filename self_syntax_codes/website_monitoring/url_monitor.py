from http.client import HTTPConnection


url_list=["python.org","http://python.org","www.python.org"]

def fetch_response_status(url):
    connection = HTTPConnection(url)
    connection.request("GET", "/")
    response = connection.getresponse()
    return response.status,response.reason

for url in url_list:
    print(url)
    print(type(url))
