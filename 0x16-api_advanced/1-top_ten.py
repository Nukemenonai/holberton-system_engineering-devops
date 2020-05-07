#!/usr/bin/python3
""" this module returns the number of subscribers """

import requests
import sys


def top_ten(subreddit):
    """
    returns the numberof subscribers of a subreddit
    """
    base = 'https://api.reddit.com/r/'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(base + subreddit + '/hot', headers=user_agent,
                     allow_redirects=False, params={"limit":10})
    if (r.status_code == 404):
        print(None)
    else:
        data = r.json()
        for item in data['data']['children']:
            print(item['data']['title'])
