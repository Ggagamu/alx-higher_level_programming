#!/usr/bin/python3
"""Module documentation for a python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    d = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = d.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
