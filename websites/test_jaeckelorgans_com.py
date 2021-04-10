import requests
import warnings

# Someday...but no SSL as of yet. :(
# from common import check_cert

# def test_cert():
#     check_cert("chandlerswift.com")
#     check_cert("www.chandlerswift.com")

def test_homepage_load():
    r = requests.get("http://jaeckelorgans.com/")
    assert r.status_code == 200
    assert "The Highest Quality Above All Else" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_www_redirect():
    r = requests.get("http://www.jaeckelorgans.com")
    assert r.url == "http://jaeckelorgans.com/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")
