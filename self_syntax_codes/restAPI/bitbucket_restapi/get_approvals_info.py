import getpass,json,requests,sys

user=raw_input("Please enter username: ")
passwd=getpass.getpass()
auth_values = (user, passwd)

url="http://tlvgit02.nice.com/rest/default-reviewers/1.0/projects/WFO/repos/"
repos=["saas-platform-ms-access-key-manager","saas-platform-ms-tenant-manager","saas-platform-ms-authentication-manager","saas-platform-ms-user-manager","saas-platform-ms-authorization-manager"]

for i in range(len(repos)):
	url=url+repos[i]+"/conditions"
    #print url,auth_values  
    r=requests.get(url, auth=auth_values)
    if (r.status_code!=200):
        print "HTTP request failed to access "+repos[i]
        #sys.exit(1)
    print "Repo: "+repos[i]+":::Approvals Required: "+str(r.json()[0]["requiredApprovals"])
    
	

