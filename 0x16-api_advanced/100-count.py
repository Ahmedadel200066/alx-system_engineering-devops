#!/usr/bin/python3
"""100-count"""
import requests


def count_words(subreddit, word_list, after='start', words_count=None):
    """
    Count the occurrences of words from a given word
    list in the titles of posts from a subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count.
        after (str, optional): The identifier of the
        post to start counting from. Defaults to 'start'.
        words_count (dict, optional): A dictionary to
        store the word counts. Defaults to None.
    Returns:
        int: 1 if the counting is successful, 0 otherwise.
    """

    if not word_list:
        return 0

    if words_count is None:
        words_count = {word: 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "u/Haisenberg"}
    if after != 'start':
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    for post in response.json().get('data').get('children'):
        title = post.get('data').get('title')
        for word in title.split():
            if word in words_count.keys():
                words_count[word] += 1

    after = response.json().get('data').get('after')
    if after:
        return count_words(subreddit, word_list, after, words_count)
    else:
        words_count = dict(sorted(words_count.items(),
                                  key=lambda x: x[1], reverse=True))
        copy = dict()
        for word, count in words_count.items():
            if word.lower() in copy.keys():
                copy[word.lower()] += count
            else:
                copy[word.lower()] = words_count[word]

        for word, count in copy.items():
            if count != 0:
                print(str(word) + ": " + str(count))
        return 1
