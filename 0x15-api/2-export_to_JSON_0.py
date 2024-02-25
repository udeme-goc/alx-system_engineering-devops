#!/usr/bin/python3

import json
import requests

def export_to_json():
    """
    Retrieves all todos from the JSONPlaceholder API and exports them
    to a JSON file.
    """
    # Step 1: Define the URL for fetching all todos
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    # Step 2: Make a GET request to fetch all todos
    response = requests.get(url_todos)
    todos = response.json()

    # Step 3: Write todos to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todos, json_file, indent=4)

if __name__ == "__main__":
    # Step 4: Call export_to_json function
    export_to_json()
