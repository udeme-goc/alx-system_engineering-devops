#!/usr/bin/python3
"""
Script to retrieve employee data from an API and display completed tasks.

This script takes an employee ID as a command-line argument and fetches the
employee's data from a REST API. It then retrieves tasks assigned to the 
employee and prints the number of completed tasks out of the total tasks, 
along with the titles of the completed tasks.

The API used in this script is 'https://jsonplaceholder.typicode.com'.

Usage:
    $ python script_name.py employee_id

Arguments:
    employee_id (int): The ID of the employee to retrieve data for.
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        # Check if the first argument is a valid integer
        if re.fullmatch(r'\d+', sys.argv[1]):
            # Convert the first argument to an integer (employee ID)
            id = int(sys.argv[1])
            
            # Request employee data from the API
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            
            # Request tasks data from the API
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            
            # Extract employee name from the response
            emp_name = req.get('name')
            
            # Filter tasks for the specific employee
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            
            # Filter completed tasks
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            
            # Print employee information
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            
            # If there are completed tasks, print them
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
