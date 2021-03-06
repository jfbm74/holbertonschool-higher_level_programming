#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameteryy
"""

from urllib import request, error
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.URLError as e:
        print('Error code: {}'.format(e.code))
