#!/usr/bin/python3
"""
this script uses the JSONplaceholder REST API
given an emplyee ID, it will return his todo list data
"""

from requests import get
from sys import argv


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com/"
    ID = argv[1]

    EMPLOYEE_NAME = get(base_url + "users",
                        params={"id": ID}).json()[0].get('name')

    TOTAL_NUMBER_OF_TASKS = get(base_url + "todos",
                                params={"userId": ID}).json()

    NUMBER_OF_DONE_TASKS = get(base_url + "todos",
                               params={"userId": ID,
                                       "completed": "true"}).json()

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME,
                  len(NUMBER_OF_DONE_TASKS),
                  len(TOTAL_NUMBER_OF_TASKS)))

    for item in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(item.get('title')))
