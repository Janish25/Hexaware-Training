import json

choice = int(input("1. SignUp \n 2. Login \n 3. Exit: \n 4.Fetch \n"))
loop = True

while loop:
    if choice == 1:
        name = input("Enter your name: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        new_data = {
            "name": name,
            "username": username,
            "password": password
        }

        with open('datas.json', 'r') as file:
            file_data = json.load(file)
        
        file_data.append(new_data)

        with open('datas.json', 'w') as file:
            json.dump(file_data, file, indent=4)

        print("Signup Successful!")

    elif choice == 2:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        
        with open('datas.json', "r") as file:
            fetchedData = json.load(file)
        
        valid = 0
        for i in fetchedData:
            if(username == i["username"]):
                if(password == i["password"]):
                    valid = 1
                    print("Logged In successfully")
                    break
        if(valid == 0):
            print("Invalid Credentials")

    elif choice == 3:
        print("Exiting...")
        loop = False
        
    elif choice == 4:
        with open('datas.json', "r")as file:
            fetchedData = json.load(file)
            
        for i in fetchedData:
            print(i)
            
    else:
        print("Invalid choice. Try again.")

    if loop:
        choice = int(input("1. SignUp \n 2. Login \n 3. Exit: \n 4.Fetch \n"))
