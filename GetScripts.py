import requests as re

def delete_quarantines(agentId):
	response = re.get('https://xxxxxxxx.helix.apps.fireeye.com/hx/api/v3/hosts/{}/quarantines'.format(agentId), verify=False  ,auth=('xxxx', 'xxxxxx'))
	after_json = response.json()
	extractData = after_json['data']['entries']
	for i in extractData:
		theIdOfFile = i['_id']
		deleteFiles = re.post('https://xxxxxxxxx.helix.apps.fireeye.com/hx/api/v3/quarantines/{}/actions/delete'.format(theIdOfFile), verify=False  ,auth=('xxxxx', 'xxxxxxxx'))
		print(deleteFiles)



def get_date():
	response = re.get('https://xxxxxxxxxx.helix.apps.fireeye.com/hx/api/v3/hosts', verify=False, auth=('xxxxx', 'xxxxxx'))
	after_json = response.json()['data']['entries']
	for i in after_json:
		num_of_files = i['stats']['malware_quarantined_count']
		hostName_of_agent = i['hostname']
		agentId = i['_id']
		who_has = hostName_of_agent + " Have " + str(num_of_files ) + " Quarantined files "
		print(who_has)
		if num_of_files > 0:
			print(agentId)
			delete_quarantines(agentId)

	
