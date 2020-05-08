#!/usr/bin/python3
""" This module return all hot titles for a subreddit """
from requests import get

BASE = "https://api.reddit.com/r/"
USER_AGENT = {'user-agent': 'david/1.0.0'}


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing the titles of all hot articles for a
    subreddit.
    """
    if after is None:
        return hot_list

    url = BASE + subreddit + "/hot"

    params = {
        'limit': 100,
        'after': after
    }

    r = get(url, headers=USER_AGENT, params=params, allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        data = r.json()
    except ValueError:
        return None

    try:
        bdata = data.get("data")
        after = bdata.get("after")
        children = bdata.get("children")
        for item in children:
            post = item.get("data")
            hot_list.append(post.get("title"))
    except:
        return None

    return recurse(subreddit, hot_list, after)
