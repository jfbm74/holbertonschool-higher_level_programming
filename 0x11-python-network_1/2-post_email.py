#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib import request, parse
from sys import argv

if __name__ == '__main__':
    mail = parse.urlencode({'email': argv[2]})
    mail = mail.encode('ascii')
    url = argv[1]
    with request.urlopen(url, mail) as response:
        html = response.read()
        print(html.decode('utf-8'))
