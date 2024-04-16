import requests
import json

# Получаем данные о задачах с удаленного сервера
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Создаем словарь для подсчета завершенных задач для каждого пользователя
completed_tasks_by_user = {}

# Подсчитываем количество завершенных задач для каждого пользователя
for todo in todos:
    if todo["completed"]:
        user_id = todo["userId"]
        if user_id in completed_tasks_by_user:
            completed_tasks_by_user[user_id] += 1
        else:
            completed_tasks_by_user[user_id] = 1

# Находим максимальное количество завершенных задач
max_completed_tasks = max(completed_tasks_by_user.values())

# Находим пользователей с максимальным количеством завершенных задач
users_with_max_completed_tasks = [user_id for user_id, num_tasks in completed_tasks_by_user.items() if num_tasks == max_completed_tasks]

# Фильтруем завершенные задачи для пользователей с userId 5 и userId 10
completed_tasks_user_5 = [todo for todo in todos if todo["userId"] == 5 and todo["completed"]]
completed_tasks_user_10 = [todo for todo in todos if todo["userId"] == 10 and todo["completed"]]

# Словарь для хранения завершенных задач для пользователей с userId 5 и userId 10
user_tasks = {"userId_5": completed_tasks_user_5, "userId_10": completed_tasks_user_10}

# Записываем данные о завершенных задачах пользователей в JSON-файл
with open("user_tasks.json", "w") as json_file:
    json.dump(user_tasks, json_file, indent=4)

# Формируем строку с информацией о пользователях с максимальным количеством завершенных задач
users_str = " and ".join(map(str, users_with_max_completed_tasks))

# Выводим информацию о пользователях с максимальным количеством завершенных задач
print(f"Пользователи {users_str} завершили {max_completed_tasks} задач(и)")