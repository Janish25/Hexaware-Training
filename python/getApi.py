import requests
import json

apiUrl = "https://jsonplaceholder.typicode.com/users"

response = requests.get(apiUrl)
users = response.json()

datas = []
for u in users:
    print(f"{u['name']} - {u['username']} - {u['address']['city']}")
    datas.append({
        'name': u['name'],
        'username': u['username'],
        'city': u['address']['city']
})

    
    
with open("user_data.json", "w") as file:
    json.dump(datas, file, indent=4)