import requests
from requests.auth import HTTPBasicAuth



##  DISABLE WARNINGS

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)



##  DEFINE URLS AND USER CREDENTIALS

TOKEN_URL = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
DEVICE_URL = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
USERNAME = 'devnetuser'
PASSWORD = 'Cisco123!'



##  RETRIEVE TOKEN

post_response = requests.post(
    TOKEN_URL,
    auth =HTTPBasicAuth(USERNAME, PASSWORD),
    verify=False
)
token = post_response.json()['Token']
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}



## GET DEVICE LIST

get_response = requests.get(
    DEVICE_URL,
    headers = headers,
    verify=False,
)

for item in get_response.json()['response']:
    print(item['id'], item['hostname'], item['managementIpAddress'])


