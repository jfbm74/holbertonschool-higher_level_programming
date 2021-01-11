#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
and user  as arguments
"""


import sys
import requests
if __name__ == "__main__":
   
    owner = sys.argv[2]
    repo = sys.argv[1]
    

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo)

    answer = requests.get(url)

    json = answer.json()

    for count, commit in enumerate(json):
        if count == 10:
            break

        print('{}: {}'.format(commit.get('sha'), commit.get(
            'commit').get('author').get('name')))
