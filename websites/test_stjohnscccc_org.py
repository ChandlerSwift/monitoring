import warnings
import requests
from common import check_cert

def test_cert():
    check_cert("stjohnscccc.com")
    check_cert("www.stjohnscccc.com")
    check_cert("stjohnscccc.org")
    check_cert("www.stjohnscccc.org")

def test_homepage_load():
    r = requests.get("https://stjohnscccc.org/")
    assert r.status_code == 200
    assert "St. John's Church" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_https_redirect():
    r = requests.get("http://stjohnscccc.org")
    assert r.url == "https://stjohnscccc.org/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_www_load():
    r = requests.get("https://www.stjohnscccc.org")
    assert r.status_code == 200
    assert "St. John's Church" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_com_redirect():
    r = requests.get("https://stjohnscccc.com/")
    # In theory this may become a redirect, but we wanted to make people notice
    assert r.status_code == 200
    assert "Looking for St. John's CCCC?" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")
