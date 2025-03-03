person = []

def addPerson(value):
    #print("person added...")
    person.append(value)
    
def display():
    i = 0
    for p in person:
        i += 1
        print(i," person: ", p)
        
def displayV2():
    for index, p in enumerate(person, 1):
        print(f"{index}. {p}")
    
addPerson("Aaron")
addPerson("Paul")

display()
displayV2()