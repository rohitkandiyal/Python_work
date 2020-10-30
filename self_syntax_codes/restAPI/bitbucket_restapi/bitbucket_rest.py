import requests,json

#this is added to make a diff of master with pull_req branch

#url="https://tlvgit02.nice.com/rest/api/1.0/projects"	//gives project details in json
url="http://tlvgit02.nice.com/rest/api/1.0/projects/~rohit.kandiyal/repos"

url="http://tlvgit02.nice.com/rest/default-reviewers/1.0/projects/~rohit.kandiyal/repos/bitbucket_restapi/conditions"

user="Rohit.Kandiyal"
passwd="P@s&nc17f"
auth_values = (user, passwd)

prj= requests.get(url, auth=auth_values)

#prj=json.loads(prj.text)			//converted to dict
a=prj.json()[0]						//converted to dict
a["requiredApprovals"]=5
url="http://tlvgit02.nice.com/rest/default-reviewers/1.0/projects/~rohit.kandiyal/repos/bitbucket_restapi/condition/"
url=url+str(a["id"])

#print a["projects"]["project"][1]		//print 1st project details

print "CURRENT PROJECTS\n"

for i in range(len(prj["projects"]["project"])):
	print prj["projects"]["project"][i]["name"]
	
	
	




