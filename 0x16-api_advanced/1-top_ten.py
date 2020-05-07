#!/usr/bin/python3
"""retrieves 10 latest posts in hot listing """

import requests

def top_ten(subreddit):
    """
    function that retrieves 10 latest post in hot listing
    """
    status_codes = [301, 302, 404]
    base = 'https://api.reddit.com/r/'
    user_agent = {'User-agent': 'david/1.0'}
    r = requests.get(base + subreddit + '/hot', headers=user_agent,
                     allow_redirects=False, params={"limit":10})
    if (r.status_code != 200):
        print(None)
    else:
        data = r.json()
        for item in data['data']['children']:
            print(item['data']['title'])
