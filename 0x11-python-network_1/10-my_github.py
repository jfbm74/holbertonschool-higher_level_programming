#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

import sys
import requests

if __name__ == "__main__":

    usr = sys.argv[1]
    pwd = sys.argv[2]

    answer = requests.get('https://api.github.com/user', auth=(usr, pwd))
    json = answer.json()
    print(json.get('id'))
