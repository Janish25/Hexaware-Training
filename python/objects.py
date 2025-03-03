todos = [
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False
  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": True
  },
  {
    "userId": 1,
    "id": 5,
    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
    "completed": False
  },
  {
    "userId": 2,
    "id": 6,
    "title": "qui ullam ratione quibusdam voluptatem quia omnis",
    "completed": False
  },
  {
    "userId": 2,
    "id": 7,
    "title": "illo expedita consequatur quia in",
    "completed": False
  },
  {
    "userId": 2,
    "id": 8,
    "title": "quo adipisci enim quam ut ab",
    "completed": True
  },
  {
    "userId": 2,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",
    "completed": False
  },
]

incomplete_todo = list(filter(lambda t: not t["completed"], todos))
completed_todo = list(filter(lambda t: t["completed"], todos))

def display():
    for i in incomplete_todo:
        print(f"Title: {i["title"]} Completed: {i["completed"]}")
        
def display2():
    for i in completed_todo:
        print(f"Title: {i["title"]} Completed: {i["completed"]}")
        
def display3(id):
    for i in todos:
        if(i["userId"]==id):
            print(f"Title: {i["title"]} UserId: {i["userId"]}")
        
display()
display2()
display3(1)