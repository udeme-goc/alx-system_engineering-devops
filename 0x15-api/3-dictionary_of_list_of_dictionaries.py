#!/usr/bin/python3
"""Python script to fetch ToDo lists of employees from a REST API."""

import json
import requests
import sys

if __name__ == '__main__':
    # URL of the REST API to fetch users
    url = "https://jsonplaceholder.typicode.com/users"

    # Send a GET request to fetch users
    resp = requests.get(url)
    
    # Extract users' data from the response
    Users = resp.json()

    # Dictionary to store ToDo lists of employees
    users_dict = {}

    # Iterate over each user
    for user in Users:
        USER_ID = user.get('id')  # Extract user ID
        USERNAME = user.get('username')  # Extract username
        
        # Construct URL to fetch ToDo tasks for the current user
        url = f'https://jsonplaceholder.typicode.com/users/{USER_ID}/todos/'
        
        # Send a GET request to fetch tasks for the current user
        resp = requests.get(url)
        
        # Extract tasks data from the response
        tasks = resp.json()
        
        # Initialize an empty list to store tasks for the current user
        users_dict[USER_ID] = []
        
        # Iterate over each task for the current user
        for task in tasks:
            # Extract task details
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            
            # Append task details to the list of tasks for the current user
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
    
    # Write the dictionary containing ToDo lists of employees to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
