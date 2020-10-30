import access_mule
import getpass,json,requests

user=raw_input("Please enter username: ")
passwd=getpass.getpass()

bearer=access_mule.AP_auth(user,passwd)
token=bearer.get_token()

if (token==None):
	print "Exception raised: Connection refused"
else:
	token=str(json.loads(token.text)["token_type"])+" "+str(json.loads(token.text)["access_token"])

print token

url="https://anypoint.mulesoft.com/accounts/api/me"
headers={"Authorization":token}

r1 = requests.get(url, headers=headers)
org_ID=str(json.loads(r1.text)["user"] ["organization"] ["id"])
print "ORG_ID  =  " + org_ID

url="https://anypoint.mulesoft.com/accounts/api/organizations/"+org_ID+"/environments"
r2 = requests.get(url, headers=headers)

#print r2.text

'''print "Available environments are:"
for number in range(json.loads(r2.text)["total"]):
	print json.loads(r2.text)["data"][number]["name"]
	print json.loads(r2.text)["data"][number]["id"]'''
	
for number in range(json.loads(r2.text)["total"]):
	if (json.loads(r2.text)["data"][number]["name"] == "Dev"):
		env_id=json.loads(r2.text)["data"][number]["id"]
		
print "ENV_ID  =  " + env_id

url="https://anypoint.mulesoft.com/hybrid/api/v1/servers"
headers={"Authorization":token,
	     "X-ANYPNT-ORG-ID":org_ID,
	     "X-ANYPNT-ENV-ID":env_id
	    }
r3 = requests.get(url, headers=headers)
print "Available environments are:"
'''for number in range(len(json.loads(r3.text)["data"])):
	print json.loads(r3.text)["data"][number]["name"]
'''
for number in range(len(json.loads(r3.text)["data"])):
	if (json.loads(r3.text)["data"][number]["name"]=="mule-dev-dxc"):
		server_id=json.loads(r3.text)["data"][number]["id"]						#this is int and not str

	


