import requests
import warnings
from common import check_cert

def test_cert():
    check_cert("isaacswift.com")
    check_cert("www.isaacswift.com")

def test_homepage_load():
    r = requests.get("https://isaacswift.com/")
    assert r.status_code == 200
    assert "Isaac" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_https_redirect():
    r = requests.get("http://isaacswift.com")
    assert r.url == "https://isaacswift.com/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")


def test_www_load():
    r = requests.get("https://www.isaacswift.com/")
    assert r.status_code == 200
    assert "Isaac" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")
