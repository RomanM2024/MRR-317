import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

completed_tasks_by_user = {}

for todo in todos:
    if todo["completed"]:
        user_id = todo["userId"]
        if user_id in completed_tasks_by_user:
            completed_tasks_by_user[user_id] += 1
        else:
            completed_tasks_by_user[user_id] = 1

max_completed_tasks = max(completed_tasks_by_user.values())

users_with_max_completed_tasks = [user_id for user_id, num_tasks in completed_tasks_by_user.items()
                                  if num_tasks == max_completed_tasks]

completed_tasks_user_5 = [todo for todo in todos if todo["userId"] == 5 and todo["completed"]]
completed_tasks_user_10 = [todo for todo in todos if todo["userId"] == 10 and todo["completed"]]

user_tasks = {"userId_5": completed_tasks_user_5, "userId_10": completed_tasks_user_10}

with open("user_tasks.json", "w") as json_file:
    json.dump(user_tasks, json_file, indent=4)

users_str = " and ".join(map(str, users_with_max_completed_tasks))

print(f"Пользователи {users_str} завершили {max_completed_tasks} задачи")
