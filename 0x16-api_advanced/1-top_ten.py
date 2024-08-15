#!/usr/bin/python3
"""0-subs"""
import requests


def top_ten(subreddit):
    """
    This function retrieves the top ten posts from
    a given subreddit on Reddit.
    Args:
    subreddit (str): The name of the subreddit to retrieve posts from.
    Returns:
    None
    Raises:
    requests.exceptions.HTTPError: 
    If there is an HTTP error during the request.
    KeyError: If there is a key error 
    while accessing the JSON response.
    ValueError: If there is a value error 
    while processing the JSON response.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Haisenberg00'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Ensure the request was successful

        data = response.json()
        posts = data['data']['children']

        for post in posts:
            print(post['data']['title'])

    except (requests.exceptions.HTTPError, KeyError, ValueError):
        print(None)
