import requests, json, csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

csv_columns = ['userId', 'id', 'title', 'completed']

with open('todos.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=csv_columns)

    writer.writeheader()

    for todo in todos:
        writer.writerow(todo)
