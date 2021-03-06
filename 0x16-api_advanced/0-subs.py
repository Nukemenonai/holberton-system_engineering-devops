#!/usr/bin/python3
""" this module returns the number of subscribers """

import requests
import sys


def number_of_subscribers(subreddit):
    """
    returns the numberof subscribers of a subreddit
    """
    base = 'https://api.reddit.com/r/'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(base + subreddit + '/about', headers=user_agent,
                     allow_redirects=False)
    if (r.status_code == 404):
        return 0
    else:
        data = r.json()
        return data['data']['subscribers']
