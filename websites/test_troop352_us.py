import warnings
import requests
from common import check_cert

def test_cert():
    check_cert("troop352.us")
    check_cert("www.troop352.us")

def test_homepage_load():
    r = requests.get("https://troop352.us/")
    assert r.status_code == 200
    assert "Troop 352" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_https_redirect():
    r = requests.get("http://troop352.us")
    assert r.url == "https://troop352.us/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_www_redirect():
    r = requests.get("https://www.troop352.us")
    assert r.url == "https://troop352.us/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")
