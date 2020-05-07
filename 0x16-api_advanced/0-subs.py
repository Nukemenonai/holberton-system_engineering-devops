#!/usr/bin/python3
""" this module returns the number of subscribers """

import requests
import sys


def number_of_subscribers(subreddit):
    """
    returns the numberof subscribers of a subreddit
    """

    base = 'https://reddit.com/r/'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(base + subreddit + '/about.json', headers=user_agent)
    data = r.json()
    try:
        return (data["data"]["subscribers"])
    except KeyError:
        return 0 
