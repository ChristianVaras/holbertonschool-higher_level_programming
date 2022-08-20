#!/usr/bin/python3
"""script that shows the header value"""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        answer = response.getheader('X-Request-Id')
        print(answer)
