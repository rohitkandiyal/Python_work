# this file is moved here from src to fix the import issue in test file.


# Third-party imports...
import requests

TODOS_URL = 'http://jsonplaceholder.typicode.com/todos'
# TODOS_URL = 'http://jsonplaceholder.typicode.coma/todos'        #if kept this then direct call will fail.Hence we mock


def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None

#
# a = get_todos()
# print(a.json())
