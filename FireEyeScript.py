import requests


def getData(url):
	response = requests.get(url, verify=True, auth=('xxxxx', 'xxxxx!'))
	response_after_json = response.json()
	# after reaching to the lowest level of the data.
	just_before_loop = response_after_json['data']['entries']
	global list_to_push_to_server 
	list_to_push_to_server = []
	for i in just_before_loop:
		list_to_push_to_server.append(i['_id'])
		#['_id']
	print(list_to_push_to_server)
	return list_to_push_to_server

def sendData(url, the_list_of_files):
		
		for i in the_list_of_files:
			after_format = url.format(i)
			response = requests.post(after_format, verify=True, auth=('xxxx', 'xxxx!'))
			print(response.content)

getData('https://xxxxxxx.helix.apps.fireeye.com/hx/api/v3/quarantines')
sendData('https://xxxxxxxxx.hex01.helix.apps.fireeye.com/hx/api/v3/quarantines/{}/actions/delete', list_to_push_to_server)

# https://<IP_address>:<port_number>/hx/api/v3/quarantines/<quarantine_id>/action/delete


hwc-hwp-6190760

4624

142.11.212.106

142.11.212.151





