#!/usr/bin/python3

import csv
import requests

def export_to_csv(employee_id):
    """
    Retrieves the todos of a given employee from the JSONPlaceholder API
    and exports them to a CSV file.
    
    Args:
        employee_id (int): The ID of the employee whose todos are to be exported.
    """
    # Step 1: Define the URL for fetching todos of the employee
    url_todos = 'https://jsonplaceholder.typicode.com/'
                'todos?userId={}'.format(employee_id)

    # Step 2: Make a GET request to fetch the todos
    response = requests.get(url_todos)
    todos = response.json()

    # Step 3: Define the fieldnames for the CSV file
    fieldnames = ['userId', 'username', 'completed', 'title']

    # Step 4: Write todos to a CSV file
    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'userId': todo['userId'],
                'username': todo['username'],
                'completed': todo['completed'],
                'title': todo['title']
            })

if __name__ == "__main__":
    # Step 5: Call export_to_csv function with employee_id as argument
    export_to_csv(1)  # Example: Export todos of employee with ID 1 to CSV

