#!/usr/bin/python3
"""2-recurse"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of the hot posts from a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of the hot posts.
    Returns:
        list: A list of strings containing the titles of the hot posts.
        None: If an error occurs during the retrieval process.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "u/Haisenberg00"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list