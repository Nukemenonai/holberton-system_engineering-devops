#!/usr/bin/python3
"""retrieves 10 latest posts in hot listing """

import requests

def top_ten(subreddit):
    """
    function that retrieves 10 latest post in hot listing
    """
    base = 'https://api.reddit.com/r/'
    user_agent = {'User-agent': 'david/1.0.0'}
    r = requests.get(base + subreddit + '/hot', headers=user_agent,
                     allow_redirects=False, params={"limit":10})
    if (r.status_code != 200):
        print(None)
        return None
    else:
        try:
            data = r.json()
        except:
            print("Not a JSON")
            return 0
        try:
            body = data.get('data')
            children = body.get('children')
            for item in children:
                post = item.get('data')
                print(post.get('title'))
        except:
            return None
