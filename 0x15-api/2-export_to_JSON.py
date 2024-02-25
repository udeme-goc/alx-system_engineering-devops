#!/usr/bin/python3
"""Python script to retrieve data from an API and convert it to JSON format."""

import csv
import json
import requests
import sys

if __name__ == '__main__':
    # Get user ID from command-line arguments
    USER_ID = sys.argv[1]

    # URL to fetch user data
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID

    # Send request to fetch user data
    res = requests.get(url_to_user)

    # Extract username from response
    USERNAME = res.json().get('username')

    # URL to fetch user's tasks
    url_to_task = url_to_user + '/todos'

    # Send request to fetch user's tasks
    res = requests.get(url_to_task)
    tasks = res.json()

    # Create dictionary to store data
    dict_data = {USER_ID: []}

    # Iterate through tasks and populate dictionary
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        })

    # Write data to JSON file
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
