#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) > 1:
        query = {'q': argv[1]}
    else:
        query = {'q': ""}
    answer = requests.post('http://0.0.0.0:5000/search_user', query)
    try:
        json = answer.json()
        if json:
            print("[{}] {}".format(json['id'],json['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
