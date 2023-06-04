import json
import requests

URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'name': 'zia',
    'roll': '101',
    'city': 'Lahore'
}
json_data = json.dump(data)


r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
