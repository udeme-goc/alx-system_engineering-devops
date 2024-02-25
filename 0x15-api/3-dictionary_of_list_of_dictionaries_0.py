#!/usr/bin/python3

import json
import requests

def generate_user_todo_dict():
    """
    Generates a dictionary of users with their corresponding todos
    fetched from the JSONPlaceholder API.
    
    Returns:
        dict: A dictionary containing users with their todos.
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
    user_todo_dict = {}

    # Step 5: Iterate over each user
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        user_todos = []

        # Step 6: Iterate over todos to find those belonging to the current user
        for todo in todos_data:
            if todo.get('userId') == user_id:
                # Step 7: Extract relevant information and append to user_todos
                user_todos.append({
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": username
                })

        # Step 8: Assign the user's todos to the user_id key in user_todo_dict
        user_todo_dict[user_id] = user_todos

    return user_todo_dict

if __name__ == "__main__":
    # Step 9: Call generate_user_todo_dict function
    user_todo_dict = generate_user_todo_dict()
    print(json.dumps(user_todo_dict, indent=4))

