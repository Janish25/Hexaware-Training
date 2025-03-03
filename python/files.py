import json

todos = [
    {
        'title': 'Complete the frontend',
        'priority': 3
    },
    {
        'title': 'Complete the backend',
        'priority': 1
    },
    {
        'title': 'Complete the UI/UX',
        'priority': 4
    },
    {
        'title': 'Complete the Testing',
        'priority': 2
    }
]

sorted_todos = sorted(todos, key = lambda s: s['priority'])

print('Sorted todos')
with open('sorted_todos.json', "w") as file:
    json.dump(sorted_todos,file, indent=4 )