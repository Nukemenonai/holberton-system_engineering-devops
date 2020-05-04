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
    ID = argv[1]

    USERNAME = get(base_url + "users",
                   params={"id": ID}).json()[0].get('username')

    TOTAL_NUMBER_OF_TASKS = get(base_url + "todos",
                                params={"userId": ID}).json()

    NUMBER_OF_DONE_TASKS = get(base_url + "todos",
                               params={"userId": ID,
                                       "completed": "true"}).json()
    data = {}
    data[ID] = []
    for item in TOTAL_NUMBER_OF_TASKS:
        data[ID].append({"task": item.get('title'),
                         "completed": item.get('completed'),
                         "username": USERNAME})

    """
    print(data)
    """
    with open('{}.json'.format(ID), 'w') as jsonfile:
        json.dump(data, jsonfile)
