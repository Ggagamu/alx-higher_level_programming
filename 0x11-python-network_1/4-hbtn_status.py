#!/usr/bin/python3
"""
Module documentation for a python script that fetches
https://alx-intranet.hbtn.io/status and prints the type
and the content of the response.
"""

import requests

if __name__ == '__main__':
    d = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print(f"\t- type: {type(data.text)}")
    print(f"\t- content: {data.text}")
