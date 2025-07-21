#!/usr/bin/python3
# import libraries
import sys
import requests

# get employee ID
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    # Fetch user info
    user_info = requests.get(url).json()

    # Fetch todo list
    todo_info = requests.get(todo_url).json()

    employee_name = user_info.get("name")

    # Filter completed tasks
    completed_tasks = [task for task in todo_info if task.get("completed")]
    total_done = len(completed_tasks)
    total_tasks = len(todo_info)

    # Print the header
    print("Employee {} is done with tasks({}/{}):".format(employee_name, total_done, total_tasks))

    # Print each completed task title
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

