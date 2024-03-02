#!/usr/bin/python3
"""
Module documentation for a python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    d = requests.get(url)
    if d.status_code >= 400:
        print("Error code: {}".format(d.status_code))
    else:
        print(d.text)
