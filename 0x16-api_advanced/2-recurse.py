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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except (requests.exceptions.HTTPError, KeyError, ValueError):
        return None
