import requests
import warnings
from common import check_cert

def test_cert():
    check_cert("chandlerswift.com")
    check_cert("www.chandlerswift.com")

def test_homepage_load():
    r = requests.get("https://www.chandlerswift.com/")
    assert r.status_code == 200
    assert "I’m a lifelong hacker" in r.text
    assert "Cloud Engineer at work, assorted hacks at home. Musician, tinkerer." in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_pgp_key_load():
    r = requests.get("https://www.chandlerswift.com/pgp.txt")
    assert r.status_code == 200
    assert "-----BEGIN PGP PUBLIC KEY BLOCK-----" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_pgp_key_bare_redirect():
    r = requests.get("https://chandlerswift.com/pgp.txt")
    assert r.status_code == 200
    assert "-----BEGIN PGP PUBLIC KEY BLOCK-----" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_https_redirect():
    r = requests.get("http://www.chandlerswift.com")
    assert r.url in ["https://chandlerswift.com/", "https://www.chandlerswift.com/"]
    assert r.status_code == 200
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_www_redirect():
    r = requests.get("https://chandlerswift.com")
    assert r.url == "https://www.chandlerswift.com/"
    assert r.status_code == 200
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_files_home():
    r = requests.get("https://files.chandlerswift.com/")
    assert r.status_code == 404
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_files_cert():
    check_cert("files.chandlerswift.com")

def test_files():
    r = requests.get("https://files.chandlerswift.com/ping.txt")
    assert r.status_code == 200
    assert r.text == "ping\n"
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")
