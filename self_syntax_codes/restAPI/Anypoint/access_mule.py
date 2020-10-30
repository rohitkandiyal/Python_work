import json,requests

url="https://anypoint.mulesoft.com/accounts/login"
headers = {'content-type': 'application/json'}

class AP_auth():
	def __init__(self,uname,passwd):
		self.uname=uname
		self.passwd=passwd
	
	def get_token(self):
		payload={"username":self.uname,"password":self.passwd}
		try:
			return requests.post(url, data=json.dumps(payload), headers=headers)
		except requests.exceptions.RequestException as self.e:
			return None
	
	'''def get_api(self,**query_parms):
		for key in query_parms.iterkeys():
			self.key=key
	'''	
		
		