#!/usr/bin/python3
"""
this script uses the JSONplaceholder REST API
given an emplyee ID, it will return his todo list data
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com/"
    ALL_USERS = get(base_url + "users").json()
    ALL_TODOS = get(base_url + "todos").json()

    data = {}
    for i in range(len(ALL_USERS)):
        ID = i + 1
        USERNAME = ALL_USERS[i].get('username')
        USR_TASKS = [item for item in ALL_TODOS if item.get('userId') == ID]
        data[ID] = []

        for item in USR_TASKS:
            data[ID].append({"username": USERNAME,
                             "task": item.get('title'),
                             "completed": item.get('completed'),
                             })

    with open('todo_all_employees.json', 'a') as jsonfile:
        json.dump(data, jsonfile)
