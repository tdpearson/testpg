import requests


def is_site_available(url):
    return requests.get(url).ok


def is_google_available():
    return is_site_available("https://google.com")


def is_github_available():
    return is_site_available("https://github.com")

