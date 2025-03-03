import json

def fetchDate():
    try:
        with open("sorted_todos.json", "r") as file:
            fetchedData = json.load(file)
            
        for i in fetchedData:
            print(i)
    except Exception as e:
        print(e)
        
fetchDate()