#!/usr/bin/python3
"""script that sends a POST request to the passed URL"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.post(url, {"email": sys.argv[2]})
    print(response.text)
