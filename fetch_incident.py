import requests

# ServiceNow credentials and instance URL
instance_url = 'https://your_instance.service-now.com/api/now/table/incident'
user = 'your_username'
password = 'your_password'

# Set the headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Fetch incidents
response = requests.get(instance_url, auth=(user, password), headers=headers)

if response.status_code == 200:
    incidents = response.json().get('result', [])
    for incident in incidents:
        print(f"Number: {incident['number']}, Short Description: {incident['short_description']}")
else:
    print(f"Error: {response.status_code}, {response.text}")
