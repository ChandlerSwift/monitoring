import warnings
import requests
from common import check_cert

def test_cert():
    check_cert("kathetrahan.com")
    check_cert("www.kathetrahan.com")

def test_homepage_load():
    r = requests.get("https://www.kathetrahan.com/")
    assert r.status_code == 200
    assert "Käthe" in r.text
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_https_redirect():
    r = requests.get("http://www.kathetrahan.com")
    assert r.url == "https://www.kathetrahan.com/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")

def test_bare_domain_redirect():
    r = requests.get("https://kathetrahan.com")
    assert r.url == "https://www.kathetrahan.com/"
    assert len(r.history) == 1
    assert r.history[0].status_code == 301
    assert r.elapsed.total_seconds() < 2
    if r.elapsed.total_seconds() > 0.5:
        warnings.warn(f"Response slow, took {r.elapsed.total_seconds()} seconds")
