#!/usr/bin/python3
"""0-subs"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers for the subreddit. Returns 0
        if the request fails or the subreddit does not exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "api_advanced/1.0.0 (by u/Haisenberg00)"}
    req = requests.get(url, headers, allow_redirects=False)

    if req.status_code == 404:
        return 0
    else:
        return req.json().get("data", {}).get("subscribers", 0)