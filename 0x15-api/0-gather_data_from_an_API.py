#!/usr/bin/python3
"""Script to fetch and display an employee's TODO list progress."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display the employee's TODO list progress."""
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    response.raise_for_status()
    user_data = response.json()
    employee_name = user_data.get('name')

    # Fetch todos data
    todos_url = f"{user_url}/todos"
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    # Calculate tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    num_done = len(done_tasks)

    # Display results
    print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    try:
        get_employee_todo_progress(employee_id)
    except requests.exceptions.HTTPError as e:
        print(f"Error accessing API: {e}")
        sys.exit(1)
