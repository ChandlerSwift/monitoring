import requests
import warnings
from common import check_cert

def test_cert():
    check_cert("home.chandlerswift.com")

def test_homepage_load():
    r = requests.get("https://home.chandlerswift.com/")
    assert r.status_code == 200
    assert "Talks I've given" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_https_redirect():
    r = requests.get("http://home.chandlerswift.com")
    assert r.url == "https://home.chandlerswift.com/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_factorio_cert():
    check_cert("factorio.chandlerswift.com")

# TODO: test factorio site?

def test_git_cert():
    check_cert("git.chandlerswift.com")

def test_files():
    r = requests.get("https://git.chandlerswift.com/")
    assert r.status_code == 200
    assert "A collection of my projects" in r.text
    assert "umdcyl/applehunt" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

# TODO: we could check to make sure the builds are there and syncing, or something
def test_asteroid_builds_load():
    r = requests.get("https://home.chandlerswift.com/asteroid/")
    assert r.status_code == 200
    assert "Index of /asteroid/" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")
