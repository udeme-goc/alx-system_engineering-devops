#!/usr/bin/python3
"""Export API data to CSV."""

import csv
import requests
import sys

def export_to_csv(user_id):
    """
    Export user's tasks from an API to a CSV file.

    Args:
        user_id (str): The ID of the user whose tasks are to be exported.

    Returns:
        None
    """
    # Construct URL to fetch user data
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    # Send request to fetch user data
    res = requests.get(url_user)

    # Extract username from response
    user_name = res.json().get('username')

    # Construct URL to fetch user's tasks
    task = f'{url_user}/todos'

    # Send request to fetch user's tasks
    res = requests.get(task)
    tasks = res.json()

    # Write data to CSV file
    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write header row
        csvwriter.writerow(['User ID', 'Username', 'Completed', 'Task Title'])

        # Write each task to CSV
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvwriter.writerow([user_id, user_name, completed, title_task])

if __name__ == '__main__':
    # Check if user ID is provided as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    # Extract user ID from command-line argument
    user_id = sys.argv[1]

    # Call function to export data to CSV
    export_to_csv(user_id)
