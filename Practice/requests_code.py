import requests
import json
import time

response = requests.get("http://localhost:3500/data/filter/region=Asia&country=India")
if response.status_code == 200:
    print('Success')
    print(response.json())
    # record = json.loads(response.json())
    print(response.content)
elif response.status_code ==404:
    print('Not found.')

time.sleep(3)

response = requests.getattr('http://localhost:3500/data/filter/region=Asia&country=India')
if response.status_code == 200:
    print('Success')
    records = json.loads(response.json())