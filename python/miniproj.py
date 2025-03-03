import requests
import json
import os
import time

def login():
    apiUrl = "https://reqres.in/api/login"
    
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    
    response = requests.post(apiUrl, json={
        'email': username,
        'password': password
    })
    
    if response.status_code == 200:
        info = response.json()
        token = info.get('token', '')

        with open('tokens.json', "w") as file:
            json.dump({'token': token}, file, indent=4)

        return token  

    print("Invalid Credentials..!!")
    return ""

def fetchAllUser():
    apiUrl = "https://reqres.in/api/users?page=2"
    response = requests.get(apiUrl)
    
    if response.status_code == 200:
        obj = response.json()
        data = obj.get('data', [])

        if not os.path.exists('data.json'):
            with open('data.json', "w") as file:
                json.dump([], file)

        with open('data.json', "r") as file:
            try:
                fetchedData = json.load(file)
            except json.JSONDecodeError:
                fetchedData = []

        for i in data:
            new_data = {
                'id': i['id'],
                'email': i['email'],
                'name': f"{i['first_name']} {i['last_name']}"
            }
            fetchedData.append(new_data)

        with open('all_datas.json', "w") as file:
            json.dump(fetchedData, file, indent=4)

        print("All users are inserted in all_datas.json")

def displayAllUsers():
    with open('all_datas.json', "r") as file:
        all_data = json.load(file)
    for i in all_data:
        print(i)

while True:
    choice = input("\n1. Login\n2. Fetch All Users\n3. Display All Users\n4. Auto Fetch\n5. Exit\nEnter your choice: ")

    if choice == "1":
        token = login()
        if token:
            print("Token:", token)

    elif choice == "2":
        fetchAllUser()

    elif choice == "3":
        displayAllUsers()
        
    elif choice == "4":
        while(True):
            fetchAllUser()
            time.sleep(30)

    elif choice == "5":
        print("Exiting...")
        break  

    else:
        print("Invalid choice. Please try again.")