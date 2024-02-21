#!/usr/bin/python3

import json
import requests

def fetch_todo_data():
    """
    Fetches data from the JSONPlaceholder API for users and their todos,
    organizes it into a dictionary, and saves it to a JSON file.
    """
    # Step 1: Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Step 2: Make GET requests to retrieve user and todo data
    users_response = requests.get(base_url + 'users')
    todos_response = requests.get(base_url + 'todos')

    # Step 3: Parse JSON data from the responses
    users_data = users_response.json()
    todos_data = todos_response.json()

    # Step 4: Create an empty dictionary to store todo data
    todo_dict = {}

    # Step 5: Iterate over each user
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        user_todos = []

        # Step 6: Iterate over todos to find those belonging to the current user
        for todo in todos_data:
            if todo.get('userId') == user_id:
                # Step 7: Extract relevant information and append to user_todos
                task = {
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                }
                user_todos.append(task)

        # Step 8: Assign the user's todos to the user_id key in todo_dict
        todo_dict[user_id] = user_todos

    # Step 9: Write the todo_dict to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_dict, json_file, indent=4)

if __name__ == "__main__":
    # Step 10: Call the fetch_todo_data function to execute the process
    fetch_todo_data()
